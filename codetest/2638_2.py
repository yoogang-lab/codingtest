import sys
from collections import deque
input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]

def bfs():
    q = deque([(0, 0)])
    visited = [[0] * M for _ in range(N)]
    visited[0][0] = 1
    cheese = []

    while q:
        cx, cy = q.popleft()
        for i in range(4):
            nx, ny = cx + dx[i], cy + dy[i]
            if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny]:
                visited[nx][ny] = 1
                if graph[nx][ny] == 0:
                    q.append((nx, ny))
                elif graph[nx][ny] == 1:
                    cnt = 0
                    for j in range(4):
                        ax, ay = nx + dx[j], ny + dy[j]
                        if 0 <= ax < N and 0 <= ay < M:
                            if graph[ax][ay] == 0 and visited[ax][ay] == 1:
                                cnt += 1
                    if cnt >= 2:
                        cheese.append((nx, ny))

    for x, y in cheese:
        graph[x][y] = 0

    return len(cheese)

def countCheese():
    return sum(graph[x][y] == 1 for x in range(N) for y in range(M))

cheeseCount = countCheese()
print(countCheese())
count = 0
while cheeseCount > 0:
    removed = bfs()
    cheeseCount -= removed
    count += 1

print(count)