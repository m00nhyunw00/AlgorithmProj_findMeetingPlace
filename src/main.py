import subway_graph
import station_info

def main():
    # 사용 예제
    subway = subway_graph.SubwayGraph()

    # 1호선 노드 생성------------------------------------------------------------------

    line1 = [station_info.line1, station_info.line1_1, station_info.line1_2, station_info.line1_3]
    subway_graph.make_stations(subway, line1)

    # 2호선 노드 생성------------------------------------------------------------------

    line2 = [station_info.line2, station_info.line2_1, station_info.line2_2]
    subway_graph.make_stations(subway, line2)

    # 3호선 노드 생성------------------------------------------------------------------

    line3 = [station_info.line3]
    subway_graph.make_stations(subway, line3)

    # 4호선 노드 생성------------------------------------------------------------------

    line4 = [station_info.line4]
    subway_graph.make_stations(subway, line4)

    # 5호선 노드 생성------------------------------------------------------------------

    line5 = [station_info.line5, station_info.line5_1]
    subway_graph.make_stations(subway, line5)

    # 6호선 노드 생성------------------------------------------------------------------

    line6 = [station_info.line6]
    subway_graph.make_stations(subway, line6)

    # 7호선 노드 생성------------------------------------------------------------------

    line7 = [station_info.line7]
    subway_graph.make_stations(subway, line7)

    # 8호선 노드 생성------------------------------------------------------------------

    line8 = [station_info.line8]
    subway_graph.make_stations(subway, line8)

    # 9호선 노드 생성------------------------------------------------------------------

    line9 = [station_info.line9]
    subway_graph.make_stations(subway, line9)

    # 수인분당선 노드 생성------------------------------------------------------------------

    lineSuinBundang = [station_info.lineSuinBundang]
    subway_graph.make_stations(subway, lineSuinBundang)

    # 신분당선 노드 생성------------------------------------------------------------------

    lineSinbundang = [station_info.lineSinbundang]
    subway_graph.make_stations(subway, lineSinbundang)

    # 경의선 노드 생성------------------------------------------------------------------

    lineGyeongui = [station_info.lineGyeongui, station_info.lineGyeongui_1]
    subway_graph.make_stations(subway, lineGyeongui)

    # 신림선 노드 생성------------------------------------------------------------------

    lineSinlim = [station_info.lineSinlim]
    subway_graph.make_stations(subway, lineSinlim)

    # 김포골드선 노드 생성------------------------------------------------------------------

    lineKimpoGold = [station_info.lineKimpoGold]
    subway_graph.make_stations(subway, lineKimpoGold)

    # 서해선 노드 생성------------------------------------------------------------------

    lineWestSea = [station_info.lineWestSea]
    subway_graph.make_stations(subway, lineWestSea)

    # 우이신설선 노드 생성------------------------------------------------------------------

    lineUii = [station_info.lineUii]
    subway_graph.make_stations(subway, lineUii)

    # 경강선 노드 생성------------------------------------------------------------------

    lineGyeonggang = [station_info.lineGyeonggang]
    subway_graph.make_stations(subway, lineGyeonggang)

    # 용인선 노드 생성------------------------------------------------------------------

    lineYongin = [station_info.lineYongin]
    subway_graph.make_stations(subway, lineYongin)

    # 의정부선 노드 생성------------------------------------------------------------------

    lineUijeongbu = [station_info.lineUijeongbu]
    subway_graph.make_stations(subway, lineUijeongbu)

    # 경춘선 노드 생성------------------------------------------------------------------

    lineGyeongchun = [station_info.lineGyeongchun, station_info.lineGyeongchun_1]
    subway_graph.make_stations(subway, lineGyeongchun)

    # 공항철도선 노드 생성------------------------------------------------------------------

    lineAirportRailroad = [station_info.lineAirportRailroad]
    subway_graph.make_stations(subway, lineAirportRailroad)

    # 인천1호선 노드 생성------------------------------------------------------------------

    lineIncheon1 = [station_info.lineIncheon1]
    subway_graph.make_stations(subway, lineIncheon1)

    # 인천2호선 노드 생성------------------------------------------------------------------

    lineIncheon2 = [station_info.lineIncheon2]
    subway_graph.make_stations(subway, lineIncheon2)

    # 1호선 노드 연결------------------------------------------------------------------

    subway_graph.connect_stations(subway, line1, "line1")

    # 2호선 노드 연결------------------------------------------------------------------

    subway_graph.connect_stations(subway, line2, "line2")

    # 3호선 노드 연결------------------------------------------------------------------

    subway_graph.connect_stations(subway, line3, "line3")

    # 4호선 노드 연결------------------------------------------------------------------

    subway_graph.connect_stations(subway, line4, "line4")

    # 5호선 노드 연결------------------------------------------------------------------

    subway_graph.connect_stations(subway, line5, "line5")

    # 6호선 노드 연결------------------------------------------------------------------

    subway_graph.connect_stations(subway, line6, "line6")

    # 7호선 노드 연결------------------------------------------------------------------

    subway_graph.connect_stations(subway, line7, "line7")

    # 8호선 노드 연결------------------------------------------------------------------

    subway_graph.connect_stations(subway, line8, "line8")

    # 9호선 노드 연결------------------------------------------------------------------

    subway_graph.connect_stations(subway, line9, "line9")

    # 수인분당선 연결------------------------------------------------------------------

    subway_graph.connect_stations(subway, lineSuinBundang, "lineSuinBundang")

    # 신분당선 연결------------------------------------------------------------------

    subway_graph.connect_stations(subway, lineSinbundang, "lineSinbundang")

    # 경의선 연결------------------------------------------------------------------

    subway_graph.connect_stations(subway, lineGyeongui, "lineGyeongui")

    # 신림선 연결------------------------------------------------------------------

    subway_graph.connect_stations(subway, lineSinlim, "lineSinlim")

    # 김포골드선 연결------------------------------------------------------------------

    subway_graph.connect_stations(subway, lineKimpoGold, "lineKimpoGold")

    # 서해선 연결------------------------------------------------------------------

    subway_graph.connect_stations(subway, lineWestSea, "lineWestSea")

    # 우이신설선 연결------------------------------------------------------------------

    subway_graph.connect_stations(subway, lineUii, "lineUii")

    # 경강선 연결------------------------------------------------------------------

    subway_graph.connect_stations(subway, lineGyeonggang, "lineGyeonggang")

    # 용인선 연결------------------------------------------------------------------

    subway_graph.connect_stations(subway, lineYongin, "lineYongin")

    # 의정부선 연결------------------------------------------------------------------

    subway_graph.connect_stations(subway, lineUijeongbu, "lineUijeongbu")

    # 경춘선 연결------------------------------------------------------------------

    subway_graph.connect_stations(subway, lineGyeongchun, "lineGyeongchun")

    # 공항철도선 연결------------------------------------------------------------------

    subway_graph.connect_stations(subway, lineAirportRailroad, "lineAirportRailroad")

    # 인천1호선 연결------------------------------------------------------------------

    subway_graph.connect_stations(subway, lineIncheon1, "lineIncheon1")

    # 인천2호선 연결------------------------------------------------------------------

    subway_graph.connect_stations(subway, lineIncheon2, "lineIncheon2")

    # subway.visualize()

    targets = []
    while True:
        # 사용자로부터 역 이름을 입력받음
        user_input = input("역을 입력하세요 (종료하려면 'q' 입력) : ")

        # 입력이 '종료'인 경우 반복문 종료
        if user_input == 'q':
            break

        # 입력된 역 이름을 리스트에 추가
        targets.append(user_input)

    # 입력한 역을 시각화하는 메소드 호출
    subway.search_node(targets)

if __name__ == "__main__":
    main()
