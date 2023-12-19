import subway_graph
import station_info
from bfs import bfs
from dfs import dfs
from dijk import dijk
from astar import astar_1, astar_2
import numpy as np

# 지하철 관련 정보 station_info.py에서 가져옴
line1 = [station_info.line1, station_info.line1_1, station_info.line1_2, station_info.line1_3]
line1_time = [station_info.line1_time, station_info.line1_1_time, station_info.line1_2_time, station_info.line1_3_time]

line2 = [station_info.line2, station_info.line2_1, station_info.line2_2]
line2_time = [station_info.line2_time, station_info.line2_1_time, station_info.line2_2_time]

line3 = [station_info.line3]
line3_time = [station_info.line3_time]

line4 = [station_info.line4]
line4_time = [station_info.line4_time]

line5 = [station_info.line5, station_info.line5_1]
line5_time = [station_info.line5_time, station_info.line5_1_time]

line6 = [station_info.line6, station_info.line6_1]
line6_time = [station_info.line6_time, station_info.line6_1_time]

line7 = [station_info.line7]
line7_time = [station_info.line7_time]

line8 = [station_info.line8]
line8_time = [station_info.line8_time]

line9 = [station_info.line9]
line9_time = [station_info.line9_time]

lineSuinBundang = [station_info.lineSuinBundang]
lineSuinBundang_time = [station_info.lineSuinBundang_time]

lineSinbundang = [station_info.lineSinbundang]
lineSinbundang_time = [station_info.lineSinbundang_time]

lineGyeongui = [station_info.lineGyeongui, station_info.lineGyeongui_1]
lineGyeongui_time = [station_info.lineGyeongui_time, station_info.lineGyeongui_1_time]

lineSinlim = [station_info.lineSinlim]
lineSinlim_time = [station_info.lineSinlim_time]

lineUii = [station_info.lineUii]
lineUii_time = [station_info.lineUii_time]

lines = [line1, line2, line3, line4, line5, line6, line7, line8, line9, lineSuinBundang, lineSinbundang
    , lineGyeongui, lineSinlim, lineUii]

lines_times = [line1_time, line2_time, line3_time, line4_time, line5_time, line6_time, line7_time, line8_time,
               line9_time, lineSuinBundang_time, lineSinbundang_time
    , lineGyeongui_time, lineSinlim_time, lineUii_time]

class User:
    def __init__(self, name):
        self.name = name
        self.position = None


def calculate_mean_and_std(data):
    # 데이터의 평균 계산
    mean_value = np.mean(data)

    # 데이터의 표준편차 계산
    std_deviation = np.std(data)

    return mean_value, std_deviation


def recommed_process(object):
    users = []

    num = 0
    while True:
        num += 1
        print(f"\n--{num}번 사용자------------------------------\n")
        user_name = input("사용자 이름을 입력하세요 ('q' 입력 시 종료): ")
        if user_name.lower() == 'q':
            break

        close_station = input(f"{user_name}의 위치(가장 가까운 역)을 입력하세요: ")
        if close_station.lower() == 'q':
            break

        user = User(user_name)
        users.append(user)
        user.position = close_station

    print('\n\n')
    meeting_places = []

    num = 0
    print("\n------------------------------------------------------------------->>")
    while True:
        num += 1
        print(f"\n--{num}번 미팅 후보지------------------------------\n")
        meeting_place = input("미팅 후보지를 입력하세요 ('q' 입력 시 종료): ")
        if meeting_place.lower() == 'q':
            break

        meeting_places.append(meeting_place)
    print("\n------------------------------------------------------------------->>\n")
    result_dfs, time_dfs, paths_dfs = recommend_algorithm(object, users, meeting_places, "Dfs")
    result_bfs, time_bfs, paths_bfs = recommend_algorithm(object, users, meeting_places, "Bfs")
    result_dijk, time_dijk, paths_dijk = recommend_algorithm(object, users, meeting_places, "Dijkstra")
    result_a1, time_a1, paths_a1 = recommend_algorithm(object, users, meeting_places, "A*1")
    result_a2, time_a2, paths_a2 = recommend_algorithm(object, users, meeting_places, "A*2")
    print
    for i in range(len(result_dfs)):
        print("DFS:")
        print(f"{result_dfs[i][0]}> 평균이동시간: 약 {int(result_dfs[i][1])}분 / 표준편차: {result_dfs[i][2]}")
        for path in paths_dfs[i]:
            print(f"------> {path[0]}: {path[1]} > 약 {path[2]}분 소요")
        print()
    for i in range(len(result_bfs)):
        print("BFS:")
        print(f"{result_bfs[i][0]}> 평균이동시간: 약 {int(result_bfs[i][1])}분 / 표준편차: {result_bfs[i][2]}")
        for path in paths_bfs[i]:
            print(f"------> {path[0]}: {path[1]} > 약 {path[2]}분 소요")
        print()
    for i in range(len(result_dijk)):
        print("Dijkstra:")
        print(f"{result_dijk[i][0]}> 평균이동시간: 약 {int(result_dijk[i][1])}분 / 표준편차: {result_dijk[i][2]}")
        for path in paths_dijk[i]:
            print(f"------> {path[0]}: {path[1]} > 약 {path[2]}분 소요")
        print()
    for i in range(len(result_a1)):
        print("A* Ver.1:")
        print(f"{result_a1[i][0]}> 평균이동시간: 약 {int(result_a1[i][1])}분 / 표준편차: {result_a1[i][2]}")
        for path in paths_a1[i]:
            print(f"------> {path[0]}: {path[1]} > 약 {path[2]}분 소요")
        print()
    for i in range(len(result_a2)):
        print("A* Ver.2:")
        print(f"{result_a2[i][0]}> 평균이동시간: 약 {int(result_a2[i][1])}분 / 표준편차: {result_a2[i][2]}")
        for path in paths_a2[i]:
            print(f"------> {path[0]}: {path[1]} > 약 {path[2]}분 소요")
        print()

    print(f"\nDfs 탐색 시간 : {time_dfs}")
    print(f"Bfs 탐색 시간 : {time_bfs}")
    print(f"Dijkstra 탐색 시간 : {time_dijk}")
    print(f"A* Ver.1 탐색 시간 : {time_a1}")
    print(f"A* Ver.2 탐색 시간 : {time_a2}")

    return


def recommend_algorithm(object, users, meeting_places, algorithm):
    entire_time = 0

    # distances, paths 초기화
    rows = len(meeting_places)
    cols = len(users)
    distances = [[0] * cols for _ in range(rows)]
    paths = [[[] for _ in range(cols)] for _ in range(rows)]

    # 추천 프로세스 진행
    for i, place in enumerate(meeting_places):
        for j, user in enumerate(users):
            path, distance, time = None, None, None
            if algorithm == "Bfs":
                path, distance, time = bfs.bfs_search(object, user.position, place)
            elif algorithm == "Dfs":
                path, distance, time = dfs.dfs_search(object, user.position, place)
            elif algorithm == "Dijkstra":
                path, distance, time = dijk.dijkstra_search(object, user.position, place)
            elif algorithm == "A*1":
                path, distance, time = astar_1.astar_search(object, user.position, place)
            elif algorithm == "A*2":
                path, distance, time = astar_2.astar_search(object, user.position, place)
            entire_time += time
            distances[i][j] = distance
            paths[i][j] = [user.name, path, distance]

    result = []
    for i, place in enumerate(meeting_places):
        mean, std = calculate_mean_and_std(distances[i])
        result.append([place, mean, std])

    return result, entire_time, paths

def main():
    subway = subway_graph.SubwayGraph()  # 지하철 노선도 그래프 생성
    # subway.visualize()  # 지하철 노선도 그래프 시각화

    for line, name in zip(lines, station_info.line_class_name):
        subway_graph.make_stations(subway, line)  # 역간 간선 생성 및 연결
        subway_graph.connect_stations(subway, line, name)  # 지하철 노드 생성

    for line, weights in zip(lines, lines_times):
        for station, weight in zip(line, weights):
            for i in range(len(weight) - 1):
                station1 = str(station[i])
                station2 = str(station[i + 1])
                subway_graph.add_weight_to_edge(subway, station1, station2, int(weight[i]))  # 간선 가중치 설정

    recommed_process(subway)  # 추천 프로세스 실행


if __name__ == "__main__":
    main()





