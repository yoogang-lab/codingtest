from collections import deque
import sys
from xmlrpc.client import MAXINT

sys.setrecursionlimit(10**6)

N = int(input())

graph = [list(map(int, input().split()))  for _ in range(N)]

dR = [0, 0, -1, 1]
dC = [1, -1, 0, 0]
DP =  [[-1] * N for _ in range(N)]



# print(graph)

maxMoveCnt = -1
maxCnt = 0

# def bfs(start) :
#     global maxMoveCnt
#     global maxCnt
#
#     visited = [[False] * N for _ in range(N)]
#     # cR, cC = start
#     queue = deque([start])
#     arr = []
#
#     while(queue) :
#         cR, cC, cMoveCnt = queue.popleft()
#         if maxMoveCnt < cMoveCnt :
#             maxMoveCnt = cMoveCnt
#             if (maxMoveCnt == 4) :
#                 print(arr)
#
#         for i in range(4) :
#             nR = cR + dR[i]
#             nC = cC + dC[i]
#             if 0<= nR < N and 0 <= nC < N :
#                 if not visited[nR][nC] and graph[cR][cC] < graph[nR][nC] :
#                     visited[nR][nC] = True
#                     arr.append((cR,cC))
#                     queue.append((nR, nC, cMoveCnt + 1))
# arr = []
def dfs(start) :
    global maxMoveCnt
    cR, cC, cMoveCnt = start
    if DP[cR][cC] > -1 :
        return DP[cR][cC]
    # DP[cR][cC] = 1

    # print(graph[cR][cC],  cMoveCnt)
    for i in range(4):
        nR = cR + dR[i]
        nC = cC + dC[i]
        if 0 <= nR < N and 0 <= nC < N and graph[cR][cC] < graph[nR][nC] :
                # visited[nR][nC] = True
                DP[cR][cC] = dfs((nR, nC, cMoveCnt + 1))
                # maxMoveCnt = max(maxMoveCnt, DP[cR][cC])
                # dp[cR][cC] = dp[nR][nj]
                # arr.pop()
                # visited[nR][nC] = False
    DP[cR][cC] = max(DP[cR][cC], cMoveCnt)
    return cMoveCnt


# minGraph = (0,0)
for i in range(N) :
    for j in range(N) :
         dfs((i, j, 1))


# print(arr)
print(DP)
print(maxMoveCnt)
