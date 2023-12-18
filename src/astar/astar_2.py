import heapq
import time
from math import radians, sin, cos, sqrt, atan2
from station_info import stations
from subway_graph import check_transfer

avg_speed = 36.0505
avg_distance = 1080.3625
avg_time = 2.2607
# 지구 반지름 길이
R = 6371.0

# 노드의 f, g, h값 및 이전 역 정보를 알기 위해 Station 클래스 선언
class Station:
    def __init__(self, name, parent=None):
        self.name = name
        self.parent = parent
        # f=g+h, 최소 힙에서 가중치 평가에 사용
        self.f = 0
        # g: 현재 역까지 오는데 걸린 시간
        self.g = 0
        # h: 종착지까지 걸릴 예상 시간
        self.h = 0

    def __eq__(self, other):
        return self.name == other.name


# heuristic: 해당 역에서 도착역까지 직선으로 이동했을 때 걸릴 예상 시간
from math import sin, cos, sqrt, atan2, radians

def heuristics(current_station, end_station):
    global avg_time, avg_distance, avg_speed, R
    
    # station_info 내의 stations에서 두 역의 위도, 경도 정보를 얻어옴
    loccur = stations[current_station.name]
    locend = stations[end_station.name]

    # 위도, 경도를 라디안으로 변환
    lat1, lon1 = radians(loccur[0]), radians(loccur[1])
    lat2, lon2 = radians(locend[0]), radians(locend[1])

    # Haversine 공식 적용
    dlat = abs(lat2 - lat1)
    dlon = abs(lon2 - lon1)

    a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    distance = R * c * 1000

    num_stations = (distance / avg_distance)

    h = num_stations * avg_time
    return h



def astar_search(object, start, end):
    start_time = time.perf_counter()

    if start not in object.graph.nodes() or end not in object.graph.nodes():
        print("출발역 또는 도착역이 그래프에 존재하지 않습니다.\n")
        return

    # 값 초기화
    start_station = Station(start)
    end_station = Station(end)
    open_list = []
    closed_list = []

    # open_list에 시작값을 넣음
    heapq.heappush(open_list, (start_station.f, start_station))

    # open_list가 없는 경우 중단 (그럴일 없음)
    while len(open_list) > 0:

        # 현재 평가값 f가 가장 작은 노드를 pop, closed에 넣음 (방문한 노드는 재방문 x)
        current_station = heapq.heappop(open_list)[1]
        closed_list.append(current_station)

        # 탐색 완료시 처리
        if current_station == end_station:
            path = []

            # 가중치 합산(실제 걸린 시간)= current_station.g
            distance = current_station.g
            tmp = current_station

            # path 리스트를 거꾸로 올라가면 경로가 나온다.
            while tmp is not None:
                path.append(tmp.name)
                tmp = tmp.parent
            print("A* 2 경로:", path[::-1])
            print("최단 거리:", distance)
            end_time = time.perf_counter()
            print("소요시간:", end_time - start_time, "\n")
            return

        children = []
        # neighbor는 역 이름
        for neighbor in object.graph.neighbors(current_station.name):
            # 새로운 객체 생성
            neighbor_station = Station(neighbor, current_station)
            children.append(neighbor_station)

        # child는 Station 객체
        for child in children:
            if child in closed_list:
                continue

            # 다음 역으로 이동할 때 시간 가중치 계산
            weight = object.graph[current_station.name][child.name]['weight']

            # 환승역 체크
            try:
                weight += check_transfer(object, current_station.parent.name, current_station.name, child.name)
            except:
                pass

            # g=현재까지 걸린 시간+추가로 걸릴 시간
            child.g = current_station.g + weight

            # h=해당 역에서 종점까지 직선거리 예상 소요시간
            child.h = heuristics(child, end_station)
            child.f = child.g + child.h

            # 탐색 중인 역이 이미 open_list에 있고, child의 이동거리가 open_list에서의 이동거리보다 긴 경우 무시
            # (더 짧은 경로가 있기 때문에 더 긴 경로를 굳이 탐색할 필요가 없다.)
            if len([open_node for open_node in open_list if child == open_node[1] and child.g > open_node[1].g]) > 0:
                continue

            heapq.heappush(open_list, (child.f, child))