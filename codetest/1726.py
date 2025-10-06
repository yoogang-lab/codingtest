from math import trunc
from xmlrpc.client import MAXINT

dR = [0, 0, 1, -1]
dC = [1, -1, 0, 0]
# 동 1.  0, 1
# 서 2.  0, -1
# 남 3.  1, 0
# 북 4. -1, 0

M, N = map(int, input().split())  # R, C

graph = [list(map(int, input().split())) for _ in range(M)]
# 방문 여부 저장
visited = [[False] * N for _ in range(M)]
minCmdCount = MAXINT

# for dd in graph:
#     print(dd)

sR, sC, sD = map(int, input().split())
eR, eC, eD = map(int, input().split())

print(eR - 1, eC - 1, eD)

def dfs (node, cmdCount) :
    global minCmdCount
    # print()
    cR, cC, cD = node

    if minCmdCount > cmdCount :
        minCmdCount = cmdCount
    if (eR - 1) == cR and (eC - 1) == cC and cD == eD :
        #제자리에서 돌기
        # lastCmdR = 0
        # lastCmdL = 0
        # if (not cD == eD) :
        #     for  i in range(4) :
        #         lastCmdR += 1
        #         if eD == (cD + (i + 1)) % 4:
        #             break
        #     for i in range(4):
        #         lastCmdL += 1
        #         if eD ==  (cD - (i + 1)) % 4 :
        #            break
        #     minCmdCount += lastCmdL if lastCmdR > lastCmdL else lastCmdR
        # print((cR, cC, cD), cmdCount)
        return

    print((cR, cC, cD),cmdCount)
    visited[cR][cC] = True

    for i in range(4) :
        nR =  cR + dR[i]
        nC =  cC + dC[i]
        # print((nR, nC))
        if 0 <= nR < M and 0 <= nC < N and not visited[nR][nC] and graph[nR][nC] == 0 :
            if not cD == (i + 1) :
                cmdCount += 1
                dfs((cR, cC, (i + 1)), cmdCount)
            else :
                cmdCount += 1
                dfs((nR, nC, (i+1)), cmdCount)


dfs((sR - 1, sC - 1, sD), 1)
print(minCmdCount)