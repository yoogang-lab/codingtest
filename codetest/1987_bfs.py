from collections import deque

R, C = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(R)]

# print(graph)
# for row in graph :
#     print(row)
dR = [0, 0, 1, -1]  # 동 1(배열 index: 0), 서 2(배열 index: 1), 남 3(배열 index: 2), 북 4(배열 index: 3)
dC = [1, -1, 0, 0]  # 동 1, 서 2, 남 3, 북 4  ( 0, 1, 2, 3)
turn = [(3,2), (2,3), (0,1), (1,0)]  # 동 쪽을 바라 보고 있다면 : 방향기준 +1,
                                     # -1(왼쪽 turn) => 0  + 1  = 1   남쪽으로 turn
                                     # +1(오른쪽 turn) => 0 - 1 =  -1 %4 => 3 북쪽으로 turn

sR, sC, sD = map(int, input().split())
eR, eC, eD = map(int, input().split())

visited = [[ [False] * 4 for _ in range(C) ] for _ in range(R)]  #3차원 배열
#최단 거리 bfs
def bfs (S):
    queue = deque([S])
    cR, cC, cD, cCmdCnt = S
    visited[cR][cC][cD] = True


    while queue :
        cq = queue.popleft()
        cR, cC, cD, cCmdCnt = cq
        # visited[cR][cC][cD] = True
        # print(cR, cC, cD ,cCmdCnt)

        if (cR == eR - 1 and cC == eC - 1 and cD == eD - 1) :
            # print("end")
            return cCmdCnt

        for i in range(1, 4):
            # print(" fdd a", i)
            nR = cR + dR[cD] * i
            nC = cC + dC[cD] * i
            if 0 <= nR < R and 0 <= nC < C and not graph[nR][nC] == 1: #직진 가능 할 경우 방문 여부 체크
                if not visited[nR][nC][cD] : # 방문 안했을 경우에만 탐색
                    queue.append((nR, nC, cD, cCmdCnt + 1))
                    visited[nR][nC][cD] = True
            else:
                break

        # for i in range(4) :
        left, right = turn[cD]
        if not visited[cR][cC][left]:
            queue.append((cR, cC, left, cCmdCnt + 1))
            visited[cR][cC][left] = True
        if not visited[cR][cC][right]:
            queue.append((cR, cC, right, cCmdCnt + 1))
            visited[cR][cC][right] = True


cmdCnt = bfs((sR - 1, sC - 1, sD - 1, 0))
print(cmdCnt)
