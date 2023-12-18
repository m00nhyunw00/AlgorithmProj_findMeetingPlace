import matplotlib.pyplot as plt
import networkx as nx
from matplotlib import rc
import station_info as si

font = 'AppleGothic'
# font = 'Malgun Gothic'

rc('font', family=font)
plt.rcParams['axes.unicode_minus'] = False

class SubwayGraph:
    def __init__(self):
        self.graph = nx.Graph()

    def update_node_class(self, station, new_class):
        # 노드가 존재하는 경우에 클래스 업데이트
        if station in self.graph.nodes():
            self.graph.nodes[station]['node_class'] = new_class
        else:
            print("없는 노드는 업데이트가 불가능합니다")

    def update_node_num_line(self, station, num_line):
        # 노드가 존재하는 경우에 num_line 업데이트
        if station in self.graph.nodes():
            self.graph.nodes[station]['num_line'] = num_line
        else:
            print("없는 노드는 업데이트가 불가능합니다")

    def get_node_class(self, station):
        # 노드의 클래스를 반환
        return self.graph.nodes[station]['node_class']

    def get_node_num_line(self, station):
        # 노드의 클래스를 반환
        return self.graph.nodes[station]['num_line']

    def add_station(self, station, node_class):
        # 이미 있는 노드인 경우 클래스를 "transfer"로 변경
        if station in self.graph.nodes():
            if self.get_node_num_line(station) == 1:
                self.update_node_class(station, "transfer2")
            elif self.get_node_num_line(station) == 2:
                self.update_node_class(station, "transfer3")
            elif self.get_node_num_line(station) == 3:
                self.update_node_class(station, "transfer4")
            elif self.get_node_num_line(station) == 4:
                self.update_node_class(station, "transfer5")
        else:
            self.graph.add_node(station, node_class=node_class, num_line=0)

    def add_connection(self, station1, station2, edge_class, weight=1):
        self.graph.add_edge(station1, station2, edge_class=edge_class, weight=weight)

    def search_node(self, targets):
        original_class = []

        # 역 이름을 강조하는 메소드
        for target in targets:
            if target in self.graph.nodes():
                original_class.append(self.get_node_class(target))
                self.update_node_class(target, "searched")
            else:
                print(f"{target}은(는) 그래프에 존재하지 않는 역입니다.")

        # 복사한 그래프를 사용하여 시각화
        self.visualize()

        i=0
        for target in targets:
            self.update_node_class(target, original_class[i])
            i+=1

    def visualize(self):
        fig, ax = plt.subplots(figsize=(20, 20))

        pos = nx.spring_layout(self.graph, k=0.1)

        class_colors_node = {"searched": "#FF0000", "general": "#DCDCDC", "transfer2": "#FF8C00",
                             "transfer3": "#008000", "transfer4": "#0000FF", "transfer5": "#800080"}
        class_colors_edge = {"line1": "#191970", "line2": "green", "line3": "#FF8C00", "line4": "#1E90FF",
                             "line5": "#8A2BE2", "line6": "#8B4513", "line7": "#6B8E23", "line8": "#FF1493",
                             "line9": "#D2B48C", "lineSuinBundang": "#FABE02", "lineSinbundang": "#D4013A", "lineGyeongui": "#0054A6",
                             "lineSinlim": "#688ACA", "lineKimpoGold": "#AD8605", "lineWestSea": "#0054A6", "lineUii": "#B8C451",
                             "lineGyeonggang": "#0054A6", "lineYongin": "#57AC2F", "lineUijeongbu": "#FB8202", "lineGyeongchun": "#0054A6",
                             "lineAirportRailroad": "#0090D2", "lineIncheon1": "#769DCF", "lineIncheon2": "#F5A352"
                             }

        node_classes = {node: data['node_class'] for node, data in self.graph.nodes(data=True)}
        edge_classes = {(node1, node2): data['edge_class'] for node1, node2, data in self.graph.edges(data=True)}
        edge_weights = {(node1, node2): data['weight'] for node1, node2, data in self.graph.edges(data=True)}

        node_colors = [class_colors_node[node_classes[node]] for node in self.graph.nodes()]
        edge_colors = [class_colors_edge[edge_classes[edge]] for edge in self.graph.edges()]

        nx.draw(self.graph, pos, with_labels=True, font_family=font, font_weight='bold',
                node_size=200, font_size=7, width=2, edge_color=edge_colors,
                node_color=node_colors, ax=ax, alpha=0.7)

        # 검색된 노드의 모양 변경
        searched_nodes = [node for node in self.graph.nodes() if node_classes[node] == 'searched']
        nx.draw_networkx_nodes(self.graph, pos, nodelist=searched_nodes, node_size=220, node_shape='s',
                               node_color='red', edgecolors='black', linewidths=1, ax=ax, alpha=0.9)

        # 간선 가중치 시각화
        # nx.draw_networkx_edge_labels(self.graph, pos, edge_labels=edge_weights)

        plt.show()


def make_stations(object, line):
    for stations in line:
        for station in stations:
            object.add_station(station, "general")
    for stations in line:
        for station in stations:
            num_line = object.get_node_num_line(station) + 1
            object.update_node_num_line(station, num_line)

def connect_stations(object, line, line_num):
    for stations in line:
        for index, station in enumerate(stations):
            if index + 1 < len(stations):
                next_station = stations[index + 1]
                object.add_connection(station, next_station, line_num)

def add_weight_to_edge(object, station1, station2, weight):
    object.graph[station1][station2]['weight'] = weight

# 매개변수는 그래프, 이전, 현재, 이동할 역 이름 문자열
def check_transfer(object, parent_station, current_station, child_station):
    
    if parent_station == None:
        return 0
    
    before = object.graph.get_edge_data(parent_station, current_station)['edge_class']
    after = object.graph.get_edge_data(current_station, child_station)['edge_class']

    station_set = {before, after}

    if before == after:
        return 0
    else:
        try:
            return si.transfer_time[current_station]
        except:
            if current_station == "청량리":
                if station_set == {"line1", "lineGyeongui"}:
                    return si.cheongryangli_time['1-경의']
                elif station_set == {"lineGyeongui", "lineSuinBundang"}:
                    return si.cheongryangli_time['경의-분당']
                elif station_set == {"lineSuinBundang", "line1"}:
                    return si.cheongryangli_time['분당-1']
                else:
                    print('청량리 오류')
                    return 0
            elif current_station == "신설동":
                if station_set == {"line1", "line2"}:
                    return si.sinseoldong_time['1-2']
                elif station_set == {"line2", "lineUii"}:
                    return si.sinseoldong_time['2-우이']
                elif station_set == {"lineUii", "line1"}:
                    return si.sinseoldong_time['우이-1']
                else:
                    print('신설동 오류')
                    return 0
            elif current_station == "종로3가":
                if station_set == {"line1", "line3"}:
                    return si.jongno3ga_time['1-3']
                elif station_set == {"line3", "line5"}:
                    return si.jongno3ga_time['3-5']
                elif station_set == {"line5", "line1"}:
                    return si.jongno3ga_time['5-1']
                else:
                    print('종로3가 오류')
                    return 0
            elif current_station == "서울역":
                if station_set == {"line1", "line4"}:
                    return si.seoul_time['1-4']
                elif station_set == {"line4", "lineGyeongui"}:
                    return si.seoul_time['4-경의']
                elif station_set == {"lineGyeongui", "line1"}:
                    return si.seoul_time['경의-1']
                else:
                    print('서울역 오류')
                    return 0
            elif current_station == "동대문역사문화공원":
                if station_set == {"line2", "line4"}:
                    return si.ddp_time['2-4']
                elif station_set == {"line4", "line5"}:
                    return si.ddp_time['4-5']
                elif station_set == {"line5", "line2"}:
                    return si.ddp_time['5-2']
                else:
                    print("DDP 오류")
                    return 0
            elif current_station == "고속터미널":
                if station_set == {"line3", "line7"}:
                    return si.gosok_time['3-7']
                elif station_set == {"line7", "line9"}:
                    return si.gosok_time['7-9']
                elif station_set == {"line9", "line3"}:
                    return si.gosok_time['9-3']
                else:
                    print("고속터미널 오류")
                    return 0
            elif current_station == "공덕":
                if station_set == {"line5", "line6"}:
                    return si.gongduk_time['5-6']
                elif station_set == {"line6", "lineGyeongui"}:
                    return si.gongduk_time['6-경의']
                elif station_set == {"lineGyeongui", "line5"}:
                    return si.gongduk_time['경의-5']
                else:
                    print("공덕 오류")
                    return 0
            elif current_station == "왕십리":
                if station_set == {"line2", "line5"}:
                    return si.wangsimni_time['2-5']
                elif station_set == {"line2", "lineSuinBundang"}:
                    return si.wangsimni_time['2-분당']
                elif station_set == {"line2", "lineGyeongui"}:
                    return si.wangsimni_time['2-경의']
                elif station_set == {"line5", "lineSuinBundang"}:
                    return si.wangsimni_time['5-분당']
                elif station_set == {"line5", "lineGyeongui"}:
                    return si.wangsimni_time['5-경의']
                elif station_set == {"lineSuinBundang", "lineGyeongui"}:
                    return si.wangsimni_time['분당-경의']
                else:
                    print("왕십리 오류")
                    return 0