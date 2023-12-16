import subway_graph
import station_info
from bfs import bfs
from dijk import dijk

def main():
    # 사용 예제
    subway = subway_graph.SubwayGraph()

    line1 = [station_info.line1, station_info.line1_1, station_info.line1_2, station_info.line1_3]
    line2 = [station_info.line2, station_info.line2_1, station_info.line2_2]
    line3 = [station_info.line3]
    line4 = [station_info.line4]
    line5 = [station_info.line5, station_info.line5_1]
    line6 = [station_info.line6]
    line7 = [station_info.line7]
    line8 = [station_info.line8]
    line9 = [station_info.line9]
    lineSuinBundang = [station_info.lineSuinBundang]
    lineSinbundang = [station_info.lineSinbundang]
    lineGyeongui = [station_info.lineGyeongui, station_info.lineGyeongui_1]
    lineSinlim = [station_info.lineSinlim]
    lineUii = [station_info.lineUii]
    lineAirportRailroad = [station_info.lineAirportRailroad]

    lines = [line1, line2, line3, line4, line5, line6, line7, line8, line9, lineSuinBundang, lineSinbundang, lineGyeongui, lineSinlim, lineUii, lineAirportRailroad]

    lines_name = ['line1', 'line2', 'line3', 'line4', 'line5', 'line6', 'line7', 'line8', 'line9', 'lineSuinBundang',
             'lineSinbundang', 'lineGyeongui', 'lineSinlim', 'lineUii', 'lineAirportRailroad']

    for line, name in zip(lines, lines_name):
        subway_graph.make_stations(subway, line)  # 역간 간선 생성 및 연결
        subway_graph.connect_stations(subway, line, name)   # 지하철 노드 생성

    # subway_graph.add_weight_to_edge(subway, '충무로', '동대입구', 2)
    # subway_graph.add_weight_to_edge(subway, '동대입구', '약수', 3)
    # subway_graph.add_weight_to_edge(subway, '약수', '금호', 1)
    # subway_graph.add_weight_to_edge(subway, '금호', '옥수', 4)
    # subway_graph.add_weight_to_edge(subway, '옥수', '압구정', 2)

    # 출발지와 목적지 입력 받기
    start_station = input("출발역을 입력하세요: ")
    end_station = input("도착역을 입력하세요: ")

    # BFS 경로 탐색
    bfs.bfs_search(subway, start_station, end_station)
    dijk.dijkstra_search(subway, start_station, end_station)

    subway.visualize()

if __name__ == "__main__":
    main()
