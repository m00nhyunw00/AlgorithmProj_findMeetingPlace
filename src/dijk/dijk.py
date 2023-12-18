import heapq
import time

def dijkstra_search(object, start_station, end_station):
    start_time = time.perf_counter()

    if start_station not in object.graph.nodes() or end_station not in object.graph.nodes():
        print("출발역 또는 도착역이 그래프에 존재하지 않습니다.\n")
        return

    # 그래프 내의 가중치를 거리라고 표현했지만, 실제로는 해당 역까지 가는데 걸린 시간임 (거리=가중치=시간으로 생각)
    # initialize
    # 그래프의 모든 노드(모든 역)의 거리를 +inf로 초기화
    distances = {node: float('inf') for node in object.graph.nodes()}
    # 시작역은 거리 0
    distances[start_station] = 0
    previous_nodes = {node: None for node in object.graph.nodes()}
    # 최소 힙 구현, heappop()의 반환값은 측정 거리(0번 인덱스 값)가 가장 작은 노드
    heap = [(0, start_station)]

    while heap:
        # 현재 측정 거리가 가장 작은 노드 pop
        current_distance, current_station = heapq.heappop(heap)

        # 큐 안의 측정값이 현재까지 측정한 거리보다 큰 경우 해당 경로 무시
        if current_distance > distances[current_station]:
            continue

        for neighbor in object.graph.neighbors(current_station):
            # 지금 분석중인 역에 대해 현재까지 측정한 거리+다음 역으로 이동하는 거리(가중치) = distance 
            weight = object.graph[current_station][neighbor]['weight']
            distance = current_distance + weight
            
            # 구한 distance 값이 기존 역의 최단거리보다 짧은 경우 update, 힙에 push
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

    if end_station not in path:
        print("경로가 존재하지 않습니다.\n")
        return

    end_time = time.perf_counter()

    print("다익스트라 경로:", path)
    print("최단 거리:", distances[end_station])
    print("소요시간:", end_time - start_time, "\n")
