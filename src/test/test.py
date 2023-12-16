from src import station_info

def compare_num_stations_times(name, stations, times):
    print(f"{name} 개수:", len(stations))
    print("소요 시간:", len(times))
    if len(stations) == len(times) + 1:
        print("O\n")
    else:
        print("X\n")

# station_info.line9_time.reverse()
# print(station_info.line9_time)

compare_num_stations_times("1", station_info.line1_1, station_info.line1_1_time)

compare_num_stations_times("1_1", station_info.line1_1, station_info.line1_1_time)

compare_num_stations_times("1_2", station_info.line1_2, station_info.line1_2_time)

compare_num_stations_times("1_3", station_info.line1_3, station_info.line1_3_time)

compare_num_stations_times("2", station_info.line2, station_info.line2_time)

compare_num_stations_times("2_1", station_info.line2_1, station_info.line2_1_time)

compare_num_stations_times("2_2", station_info.line2_2, station_info.line2_2_time)

compare_num_stations_times("3", station_info.line3, station_info.line3_time)

compare_num_stations_times("4", station_info.line4, station_info.line4_time)

compare_num_stations_times("5", station_info.line5, station_info.line5_time)

compare_num_stations_times("6", station_info.line6, station_info.line6_time)

compare_num_stations_times("6_1", station_info.line6_1, station_info.line6_1_time)

compare_num_stations_times("SuinBundang", station_info.lineSuinBundang, station_info.lineSuinBundang_time)

compare_num_stations_times("Sinbundang", station_info.lineSinbundang, station_info.lineSinbundang_time)

compare_num_stations_times("Gyeongui", station_info.lineGyeongui, station_info.lineGyeongui_time)

compare_num_stations_times("Gyeongui_1", station_info.lineGyeongui_1, station_info.lineGyeongui_1_time)

compare_num_stations_times("Sinlim", station_info.lineSinlim, station_info.lineSinlim_time)

compare_num_stations_times("Uii", station_info.lineUii, station_info.lineUii_time)

compare_num_stations_times("AirportRailroad", station_info.lineAirportRailroad, station_info.lineAirportRailroad_time)





