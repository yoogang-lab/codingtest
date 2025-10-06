import sys
from copy import deepcopy

input = sys.stdin.readline
from collections import deque

N, M = map(int, input().split())
# print(N, M)

graph = list(list(map(int, input().split())) for _ in range(M))


# print(graph)

dx = [-1, 1, 0, 0]
dy = [0, 0 , -1 ,1]

result = 9999999999999
countTomato = 0
flagBfs = False

def bfs(S) :
    queue = deque([])
    for item in S :
        queue.append(item)
    time = 0


    while queue:
        # print( "Dsadd " , queue.popleft())
        # print("pre" , queue)
        cx, cy, ct = queue.popleft()

        time = ct
        # print("\n")
        # print(queue)
        # print(cx, cy, ct)
        # for i in range(M):
            # print(visited[i])

        for i in range(4) :
            nx = cx + dx[i]
            ny = cy + dy[i]
            if (0 <= nx < M and 0 <= ny < N) :
                # print("pre", visited[nx][ny])
                if (visited[nx][ny] == 0) :
                    visited[nx][ny] = 1
                    # print("post")
                    queue.append((nx, ny, ct + 1))

    return time


startList = []
for x in range(M) :
    for y in range(N) :
        if (graph[x][y] == 1) :
            startList.append((x,y,0))
            # resultTmp = bfs(x, y)
            # flagBfs = True
            # if (result  > resultTmp ) :
            #     result = resultTmp

visited = deepcopy(graph)
result = bfs(startList)
if len(startList) == 0 :
    result = 0

for x in range(M) :
    for y in range(N) :
        if (visited[x][y] == 0) :
            result = -1

print(result)
