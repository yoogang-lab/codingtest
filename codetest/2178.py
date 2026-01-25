# https://www.acmicpc.net/problem/2178
import sys
input = sys.stdin.readline
from collections import deque
# 4 6
# 101111
# 101010
# 101011
# 111011

N, M = map(int, input().split())
graph = list(list(map(int, input().strip())) for _ in range(N))
visited = list([0] * M for _ in range(N))

# print(N, M)
# print(graph)
# print(visited)

# 미로에서 1은 이동할 수 있는 칸을 나타내고, 0은 이동할 수 없는 칸을 나타낸다. 이러한 미로가 주어졌을 때, (1, 1)에서 출발하여 (N, M)의 위치로 이동할 때 지나야 하는 최소의 칸 수를 구하는 프로그램을 작성하시오. 한 칸에서 다른 칸으로 이동할 때, 서로 인접한 칸으로만 이동할 수 있다.
# 위의 예에서는 15칸을 지나야 (N, M)의 위치로 이동할 수 있다. 칸을 셀 때에는 시작 위치와 도착 위치도 포함한다.

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
sol = 0

def bfs(S) :
    queue = deque([S])
    visited[S[0]][S[1]] = 1
    # print(queue.popleft())
    # queue.append(2)
    # print(queue.popleft())

    while queue :
        current = queue.popleft()
        cx, cy, cCount = current
        # print(cx, cy, cCount)

        if cx == N -1 and cy == M - 1 :
            sol = cCount
            print(sol)
            break

        for i in range(0, 4) :
            nx = dx[i] + cx
            ny = dy[i] + cy
            if not (0 <= nx and 0 <= ny and nx < N and ny < M) :
                continue
            # print(nx, ny)
            if not visited[nx][ny] == 1 and graph[nx][ny] == 1 :
                visited[nx][ny] = 1
                queue.append((nx,ny, cCount + 1))




bfs((0,0,1))
# print(sol)




