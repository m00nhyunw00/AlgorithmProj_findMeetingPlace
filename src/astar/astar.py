import heapq
import time
from math import radians, sin, cos, sqrt, atan2
from station_info import stations

class Station:
    def __init__(self, name, parent=None):
        self.name = name
        self.parent = parent
        self.f=0
        self.g=0
        self.h=0
    
    def __eq__(self, other):
        return self.name == other.name

def heuristics(current_station, end_station):
    R=6371.0
    speed = 33.6
    loccur = stations[current_station.name]
    locend = stations[end_station.name]
    diff_lat = abs(loccur[0] - locend[0])
    diff_log = abs(loccur[1] - locend[1])

    a = sin(diff_lat/2)**2 + cos(loccur[0]) * cos(locend[0]) * sin(diff_log/2)**2
    c = 2 * atan2(sqrt(a), sqrt(1-a))

    distance = R*c
    h = distance/speed
    return h

def astar_search(object, start, end):
    start_time = time.time()

    if start not in object.graph.nodes() or end not in object.graph.nodes():
        print("출발역 또는 도착역이 그래프에 존재하지 않습니다.\n")
        return
    
    start_station = Station(start)
    end_station = Station(end)
    open_list = []
    closed_list = []
    heapq.heappush(open_list, (start_station.f, start_station))
    
    while len(open_list)>0:
        current_station = heapq.heappop(open_list)[1]
        closed_list.append(current_station)

        # 탐색 완료시 처리
        if current_station == end_station:
            end_time = time.time()
            path=[]
            distance = current_station.g
            tmp = current_station
            while tmp is not None:
                path.append(tmp.name)
                tmp=tmp.parent
            print("A* 경로:", path.reverse())
            print("최단 거리:", distance)
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

            # g=현재까지 걸린 시간+추가로 걸릴 시간
            child.g = current_station.g + weight

            # h=해당 역에서 종점까지 직선거리 예상 소요시간
            child.h = heuristics(child, end_station)
            child.f = child.g+child.h
            
            # Child is already in the open list
            if len([open_node for open_node in open_list if child == open_node[1] and child.g > open_node[1].g]) > 0:
                continue

            heapq.heappush(open_list, (child.f, child))
