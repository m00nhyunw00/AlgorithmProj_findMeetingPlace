from src import station_info

def compare_num_stations_times(name, stations, times):
    print(f"{name} 개수:", len(stations))
    print("소요 시간:", len(times))
    if len(stations) == len(times) + 1:
        print("O\n")
    else:
        print("X\n")

# station_info.line2.reverse()
# print(station_info.line2)

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



