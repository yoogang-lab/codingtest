import sys
input = sys.stdin.readline
import heapq
INF = 1e8
# TestValue
# 5
# 6
# 1 2 1
# 1 3 3
# 2 3 1
# 2 4 5
# 3 4 2
# 5 1 1
# 1 4

N = int(input())
M = int(input())

listData =  list(list(map(int, input().split())) for _ in range(M))
distance = [INF]  * (N + 1)
visited = [False] * (N + 1)
# print(graph)
# print(visited)

S, D = map(int, input().split())

graph = [[] for _ in  range(N + 1)]
print(graph)
for s, d, v in listData :
    graph[s].append((d,v))
print(graph)
#

def dijkstra(start) :
    pq = []
    heapq.heappush(pq,(0, start))
    distance[start] = 0


    while pq :
        print("pq", pq)
        print(distance)
        dist, now = heapq.heappop(pq)
        print("dist", dist, now)
        print("pq1", pq)

        if distance[now] < dist :
            continue #중복값 제거
        print("pq2")
        for d, v in graph[now] :
            if dist + v < distance[d] :
                distance[d] = dist + v
                heapq.heappush(pq, (dist + v,d))

dijkstra(S)
print(distance[D])

