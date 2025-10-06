import collections
from collections import deque
# from xmlrpc.client import MAXINT
import sys
from collections import deque
import heapq
# input = sys.stdin.readline
INF = float('inf')

V, E = map(int, input().split())
S = int(input())
# arr = list(list(map(int, input().split())) for _ in range(E))

#print(V, E, S , arr)

graph = list([] for _ in range(V + 1))
# w = list(list(9999  for _ in range(V + 1) ) for _ in range(V + 1))
weightList = [INF] * (V + 1)
weightList[S] = 0

for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))
# print(graph)
#
# for item in arr :
#     graph[item[0]].append((item[1],item[2]))
    # graph[item[1]].append((item[0], item[2]))

# print(graph)
# print(w)

# def bfs(start) :
#     q = deque([(start, w[start][start])])
#     visited = [False] * int(V + 1)
#     visited[start] = True
#
#     while(q) :
#         cVW = q.popleft()
#         cV, cW = cVW
#
#         for nVW in graph[cV] :
#             nV, nW = nVW
#             if not visited[nV] and w[start][nV] > cW + nW :
#                 w[start][nV] = cW + nW
#                 visited[nV] = True
#                 q.append((nV, cW + nW))

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))  # (거리, 노드)

    while q:
        current_dist, current_node = heapq.heappop(q)

        # 이미 더 짧은 경로가 있으면 무시
        if current_dist > weightList[current_node]: #가중치 리스트 중에서 제일 가중치가 적은것
            continue

        for neighbor, weight in graph[current_node]:
            new_dist = current_dist + weight
            if new_dist < weightList[neighbor]:
                weightList[neighbor] = new_dist
                heapq.heappush(q, (new_dist, neighbor))



# for index in range(V) :
# bfs(S)
dijkstra(S)
# print(w[S])

for i in range(1, V + 1):
    print("INF" if weightList[i] == INF else weightList[i])







