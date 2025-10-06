N = int(input())
graph = list(list(map(int, input().strip())) for _ in range(N))
# print(graph)
dR = [0,0,1,-1]
dC = [1,-1, 0, 0]

check = 2
resultCount = []
depthResult = 0

def dfs(start, checkMark) :
    r,c = start
    graph[r][c] = checkMark
    depth = 0

    for i in range(4) :
        nR, nC = r + dR[i], c + dC[i]
        if  0 <= nR < N and 0 <= nC < N  and graph[nR][nC] == 1:
         depth += dfs((nR,nC), checkMark) + 1

    return depth


for i in range(N) :
    for j in range(N) :
        if graph[i][j] == 1 :
            resultCount.append( dfs((i,j), check) + 1)
            check +=1


# print(graph)
resultCount.sort()
print(check - 2)
for item in resultCount :
    print(item)