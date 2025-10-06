import sys
from collections import deque

N, M = map(int, input().split())
r, c, d = map(int, input().split())
visited = [[False] * M for _ in range(N)]

colDirection = [0, 1, 0, -1]
rowDirection = [-1, 0, 1, 0]
graph =[[] for _ in range(N)]

# global result
def dfs(curr, curc, curdir) :

    global result
    print(curr, curc, curdir)
    # graph 출력 추가

    graph[curr][curc] = 2
    result += 1
    for row in graph:
        print(row)
    curdir2 =  curdir
    for i in range(4):
        curdir  = (curdir + 3) % 4
        nextRow = curr + rowDirection[curdir]
        nextCol = curc + colDirection[curdir]
        if 0<=nextRow < N and 0<= nextCol < M and graph[nextRow][nextCol] == 0:
            dfs(nextRow, nextCol, curdir)
            return
    br, bc = curr - rowDirection[curdir2], curc - colDirection[curdir2]
    if 0 <= br < N and 0 <= bc < M and graph[br][bc] == 0:
          dfs(br, bc, curdir2)
    return


# read_matrix()
result = 0
dfs(r, c, d)
print(result)
