from collections import deque
import sys
from copy import deepcopy
sys.setrecursionlimit(10000)

N = int(input())

graph = [list(input().strip()) for _ in range(N)]
# print(graph)
graph2 = deepcopy(graph)
# print(graph2)
visitedNormal = [[False ] * N for _ in range(N)]
# print(visitedNormal)
visitedABNormal = [[False]  * N for _ in range(N)]
dR = [0, 0, 1, -1]
dC = [1, -1, 0, 0]


normal, abnormal = (0, 0)

def dfs(cR, cC, v, g, cColor, cColor2) :
    global  normal
    global  abnormal

    for i in range(4) :
        nR = cR + dR[i]
        nC = cC + dC[i]
        if 0 <= nR < N and 0 <=nC < N and (g[nR][nC] == cColor or (not cColor2 == '' and g[nR][nC] == cColor2)):
            g[nR][nC] = 0
            dfs(nR, nC, v, g, cColor, cColor2)


for i in range(N)  :
    for j in range(N) :
        if not graph[i][j] == 0 :
            normal += 1
            dfs(i, j,  visitedNormal, graph, graph[i][j],'')
# print(graph)
# print(graph2)
for i in range(N)  :
    for j in range(N) :
        if not graph2[i][j] == 0 :
            abnormal += 1
            if graph2[i][j] == 'R' or graph2[i][j] == 'G' :
                dfs(i, j, visitedABNormal, graph2, 'R', 'G')
            else :
                dfs(i, j, visitedABNormal, graph2, 'B','')


print(normal, abnormal)