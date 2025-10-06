from collections import deque
import sys

sys.setrecursionlimit(10 ** 6)

N = int(input())
arr = list(list(map(int, input().split())) for _ in range(N))

# print(arr)
graph = list([] for _ in range(N + 1))  # 1부터 시작

for index in range (N) :
    # print(index)
    # print(arr[index][0])
    # print(arr[index][1])
    graph[arr[index][0]].append(arr[index][1])
    graph[arr[index][1]].append(arr[index][0])
    #양방향 그래프

visitedCircular = [0 for _ in range(N + 1)]
result = [0 for _ in range(N + 1)]
visited = [0 for _ in range(N + 1)]
# print(graph)
# print(visited)

def bfs(start) :
    q = deque([(start, 0)])
    visited[start] = 1

    while(q) :
        c,n = q.popleft()
        if (visitedCircular[c] == 2) :
            return n
        for nodeItem in graph[c] :
            if visited[nodeItem] == 0 :
                visited[nodeItem] = 1
                q.append((nodeItem, n + 1))
    return 0





# def dfs(departure, arr, depth) : #순환 찾기
#     # print("visit ", departure, depth, arr)
#     if (depth >= 3 and departure == arr) :
#         return 2
#
#     for node in graph[departure] :
#         if visited[node] == 0 or (node == arr and depth >= 2) : # notvisited
#            visited[node] = 1
#            value = dfs(node, arr, depth + 1)
#            # if not visited[node] == 2 :
#            visited[node] = 0
#            if value == 2  :
#              visitedCircular[node] = 2 # 2로표시
#     return -1
def dfs(cur, start, depth):
    for nxt in graph[cur]:
        # 아직 방문 안 했으면 탐색
        if not visited[nxt]:
            visited[nxt] = 1
            if dfs(nxt, start, depth + 1) == 2:
                visitedCircular[cur] = 2
                return 2
            visited[nxt] = 0  # 백트래킹

        # 시작점으로 돌아왔고, 깊이가 3 이상이면 사이클
        elif nxt == start and depth >= 3:
            visitedCircular[cur] = 2
            return 2
    return -1

for start in range(1, N+1) :
    visited = [0 for _ in range(N + 1)]
    visited[start] = 1
    # print("=====")
    dfs(start, start, 0)

for start in range(1, N+1) :
    visited = [0 for _ in range(N + 1)]
    result[start] = bfs(start)
result.remove(0)
print(*result)




