import heapq
import time

def dijkstra_search(object, start_station, end_station):
    start_time = time.time()

    if start_station not in object.graph.nodes() or end_station not in object.graph.nodes():
        print("출발역 또는 도착역이 그래프에 존재하지 않습니다.")
        return

    # 초기화
    distances = {node: float('inf') for node in object.graph.nodes()}
    distances[start_station] = 0
    previous_nodes = {node: None for node in object.graph.nodes()}
    heap = [(0, start_station)]

    while heap:
        current_distance, current_station = heapq.heappop(heap)

        if current_distance > distances[current_station]:
            continue

        for neighbor in object.graph.neighbors(current_station):
            weight = object.graph[current_station][neighbor]['weight']
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous_nodes[neighbor] = current_station
                heapq.heappush(heap, (distance, neighbor))

    # 경로 출력
    path = []
    current = end_station

    while current is not None:
        path.insert(0, current)
        current = previous_nodes[current]

    end_time = time.time()

    print("다익스트라 경로:", path)
    print("최단 거리:", distances[end_station])
    print("소요시간:", end_time - start_time, "\n")
