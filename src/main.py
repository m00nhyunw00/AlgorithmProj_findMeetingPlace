import subway_graph
import station_info

def main():
    # 사용 예제
    subway = subway_graph.SubwayGraph()

    # 1호선 노드 생성------------------------------------------------------------------

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
    lineKimpoGold = [station_info.lineKimpoGold]
    lineWestSea = [station_info.lineWestSea]
    lineUii = [station_info.lineUii]
    lineGyeonggang = [station_info.lineGyeonggang]
    lineYongin = [station_info.lineYongin]
    lineUijeongbu = [station_info.lineUijeongbu]
    lineGyeongchun = [station_info.lineGyeongchun, station_info.lineGyeongchun_1]
    lineAirportRailroad = [station_info.lineAirportRailroad]
    lineIncheon1 = [station_info.lineIncheon1]
    lineIncheon2 = [station_info.lineIncheon2]

    lines = [line1, line2, line3, line4, line5, line6, line7, line8, line9, lineSuinBundang, lineSinbundang, lineGyeongui, lineSinlim, lineKimpoGold,
             lineWestSea, lineUii, lineGyeonggang, lineYongin, lineUijeongbu, lineGyeongchun, lineAirportRailroad, lineIncheon1, lineIncheon2]

    lines_name = ['line1', 'line2', 'line3', 'line4', 'line5', 'line6', 'line7', 'line8', 'line9', 'lineSuinBundang',
             'lineSinbundang', 'lineGyeongui', 'lineSinlim', 'lineKimpoGold', 'lineWestSea', 'lineUii',
             'lineGyeonggang', 'lineYongin', 'lineUijeongbu', 'lineGyeongchun', 'lineAirportRailroad', 'lineIncheon1',
             'lineIncheon2']

    for line in lines:
        subway_graph.make_stations(subway, line)    # 지하철 노드 생성

    for line, name in zip(lines, lines_name):   # 역간 간선 생성 및 연결
        subway_graph.connect_stations(subway, line, name)
        print(name)

    # subway.visualize()

    targets = []
    while True:
        # 사용자로부터 역 이름을 입력받음
        user_input = input("역을 입력하세요 (종료하려면 'q' 입력) : ")

        # 입력이 'q'인 경우 반복문 종료
        if user_input == 'q':
            break

        # 입력된 역 이름을 리스트에 추가
        targets.append(user_input)

    # 입력한 역을 시각화하는 메소드 호출
    subway.search_node(targets)


if __name__ == "__main__":
    main()
