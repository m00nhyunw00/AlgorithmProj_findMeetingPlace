import subway_graph
import station_info
from bfs import bfs_search
from dijk import dijk_search
from astar import astar_search
from new import bidirectional_astar_search

def main():
    # 사용 예제
    # 지하철노선도 그래프 생성
    subway = subway_graph.SubwayGraph()

    # 각 호선별 이름 및 이동 시간(가중치) 정보를 station_info.py에서 가져옴
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

    lineAirportRailroad = [station_info.lineAirportRailroad]
    lineAirportRailroad_time = [station_info.lineAirportRailroad_time]

    lines_name = ['line1', 'line2', 'line3', 'line4', 'line5', 'line6', 'line7', 'line8', 'line9', 'lineSuinBundang', 'lineSinbundang'
             , 'lineGyeongui', 'lineSinlim', 'lineUii', 'lineAirportRailroad']

    lines = [line1, line2, line3, line4, line5, line6, line7, line8, line9, lineSuinBundang, lineSinbundang
             , lineGyeongui, lineSinlim, lineUii, lineAirportRailroad]

    lines_times = [line1_time, line2_time, line3_time, line4_time, line5_time, line6_time, line7_time, line8_time, line9_time, lineSuinBundang_time, lineSinbundang_time
             , lineGyeongui_time, lineSinlim_time, lineUii_time, lineAirportRailroad_time]


    for line, name in zip(lines, lines_name):
        subway_graph.make_stations(subway, line)  # 역간 간선 생성 및 연결
        subway_graph.connect_stations(subway, line, name)   # 지하철 노드 생성

    # 간선 가중치 지정
    for line, weights in zip(lines, lines_times):
        for station, weight in zip(line, weights):
            for i in range(len(weight) - 1):
                station1 = str(station[i])
                station2 = str(station[i + 1])
                # station[i], station[i+1] 간 가중치를 weight[i]로 지정
                subway_graph.add_weight_to_edge(subway, station1, station2, int(weight[i]))


    # 출발지와 목적지 입력 받기
    start_station = input("출발역을 입력하세요: ")
    end_station = input("도착역을 입력하세요: ")
    print('\n')

    bfs = bfs_search
    dijk = dijk_search
    astar = astar_search
    bidirectional_astar = bidirectional_astar_search

    # 알고리즘 별 경로 탐색
    bfs.bfs_search(subway, start_station, end_station)
    dijk.dijkstra_search(subway, start_station, end_station)
    astar.astar_search(subway, start_station, end_station)
    bidirectional_astar.bidirectional_astar_search(subway, start_station, end_station)

    subway.visualize()

if __name__ == "__main__":
    main()
