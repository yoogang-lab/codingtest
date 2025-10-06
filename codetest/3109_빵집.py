import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

R, C = map(int, input().split())
dR = [-1,0,1]
dC = [1,1,1]
#?대각선 위, 오른쪽 , 대각선 아래 으로 순서로 최대한 위에서부터 내려왔다면, 위에서 부터 탐색하도록해야함.(그리디 알고리즘)


# print(R, C)
grid = list(list(map(str, input().strip())) for _ in range(R))
visited = list([False] * C  for _ in range (R))
pipeCnt = 0

# print(grid)
# print(visited)

def dfs (S) :
    cR, cC = S
    visited[cR][cC] = True

    if cC == C - 1 :
        return True

    for i in range(3) :
        nR, nC = cR + dR[i], cC + dC[i]
        # print(cR, dR[i], cC, dC[i])
        # print(nR, nC)

        if (0<= nR < R and 0 <= nC < C and grid[nR][nC] =='.' and not visited[nR][nC]) :
            print(nR, nC)

            #이전에   return dfs((nR, nC))   해버려서 무조건 리턴되어 다음으로 진행 안됨
            if (dfs((nR,nC))) :
                return True


    return False

for i in range(R) :
    print((i,0))
    if (dfs((i,0))) :
        pipeCnt += 1

# print(grid)
# print(visited)

for i in range(R) :
    print(grid[i])
for i in range(R) :
    print(visited[i])

print(pipeCnt)
