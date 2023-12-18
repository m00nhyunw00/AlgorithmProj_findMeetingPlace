import heapq
import time
from math import radians, sin, cos, sqrt, atan2
from station_info import stations

class Station:
    def __init__(self, name, parent=None):
        self.name = name
        self.parent = parent
        self.f = 0
        self.g = 0
        self.h = 0

    def __eq__(self, other):
        return self.name == other.name


def heuristics(current_station, end_station):
    R = 6371.0
    speed = 33.6
    loccur = stations[current_station.name]
    locend = stations[end_station.name]
    diff_lat = abs(loccur[0] - locend[0])
    diff_log = abs(loccur[1] - locend[1])
    a = sin(diff_lat / 2) ** 2 + cos(loccur[0]) * cos(locend[0]) * sin(diff_log / 2) ** 2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    distance = R * c
    h = distance / speed
    return h


def bidirectional_astar_search(object, start, goal):
    start_time = time.perf_counter()
    if start not in object.graph.nodes() or goal not in object.graph.nodes():
        print("출발역 또는 도착역이 그래프에 존재하지 않습니다.\n")
        return

    start_station = Station(start)
    goal_station = Station(goal)

    # 각 방향에서의 open_list, closed_list를 따로 유지
    open_list_start = [(start_station.f, start_station)]
    open_list_goal = [(goal_station.f, goal_station)]
    closed_list_start = []
    closed_list_goal = []

    while open_list_start and open_list_goal:
        # 시작 지점에서 탐색
        current_station_start = heapq.heappop(open_list_start)[1]
        closed_list_start.append(current_station_start)

        # 목표 지점에서 탐색
        current_station_goal = heapq.heappop(open_list_goal)[1]
        closed_list_goal.append(current_station_goal)

        # 양쪽에서 만나는 교차점 찾기
        intersection = None
        for station in closed_list_start:
            if station in closed_list_goal:
                intersection = station
                break

        if intersection:
            end_time = time.perf_counter()
            path_start = []
            path_goal = []

            # 시작 지점에서의 경로 구성
            tmp = intersection
            while tmp is not None:
                path_start.append(tmp.name)
                tmp = tmp.parent

            # 목표 지점에서의 경로 구성
            tmp = intersection.parent
            while tmp is not None:
                path_goal.append(tmp.name)
                tmp = tmp.parent

            # 양쪽 경로를 합쳐 전체 경로 구성
            path = path_start[::-1] + path_goal
            distance = intersection.g
            print("Bidirectional A* 경로:", path)
            print("최단 거리:", distance)
            print("소요시간:", end_time - start_time, "\n")
            return

        # 시작 지점에서의 확장
        children_start = [Station(neighbor, current_station_start) for neighbor in
                          object.graph.neighbors(current_station_start.name)]

        for child_start in children_start:
            if child_start in closed_list_start:
                continue

            weight_start = object.graph[current_station_start.name][child_start.name]['weight']
            child_start.g = current_station_start.g + weight_start
            child_start.h = heuristics(child_start, goal_station)
            child_start.f = child_start.g + child_start.h

            if len([open_node for open_node in open_list_start if
                    child_start == open_node[1] and child_start.g > open_node[1].g]) > 0:
                continue

            heapq.heappush(open_list_start, (child_start.f, child_start))

        # 목표 지점에서의 확장
        children_goal = [Station(neighbor, current_station_goal) for neighbor in
                         object.graph.neighbors(current_station_goal.name)]

        for child_goal in children_goal:
            if child_goal in closed_list_goal:
                continue

            weight_goal = object.graph[current_station_goal.name][child_goal.name]['weight']
            child_goal.g = current_station_goal.g + weight_goal
            child_goal.h = heuristics(child_goal, start_station)
            child_goal.f = child_goal.g + child_goal.h

            if len([open_node for open_node in open_list_goal if
                    child_goal == open_node[1] and child_goal.g > open_node[1].g]) > 0:
                continue

            heapq.heappush(open_list_goal, (child_goal.f, child_goal))

    print("경로를 찾을 수 없습니다.")
