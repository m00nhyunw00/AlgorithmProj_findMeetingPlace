from queue import Queue
import time

def bfs_search(object, start_station, end_station):
    start_time = time.time()

    if start_station not in object.graph.nodes() or end_station not in object.graph.nodes():
        print("출발역 또는 도착역이 그래프에 존재하지 않습니다.")
        return

    visited = set()
    queue = Queue()
    path = {}

    queue.put(start_station)
    visited.add(start_station)

    while not queue.empty():
        current_station = queue.get()

        for neighbor in object.graph.neighbors(current_station):
            if neighbor not in visited:
                queue.put(neighbor)
                visited.add(neighbor)
                path[neighbor] = current_station

                if neighbor == end_station:
                    # 경로가 찾아졌으면 탐색 종료
                    queue.queue.clear()
                    break

    if end_station not in path:
        print("경로가 존재하지 않습니다.")
        return

    # 경로 출력
    current = end_station
    path_list = [current]

    while current != start_station:
        current = path[current]
        path_list.append(current)

    path_list.reverse()

    end_time = time.time()

    print("BFS 경로:", path_list)
    print("소요시간:", end_time - start_time, "\n")