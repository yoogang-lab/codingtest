
R, C = map(int, input().split())
visited = [[0] * C for _ in range(R)]
# graph = [[input().split()] for _ in range(C) for _ in range(R)]
graph = [list(input().strip()) for _ in range(R)]
print(graph)

dR = [0, 0,1,-1]
dC = [1,-1,0,0]
alphabetList = [chr(ord('A') + i) for i in range(C)]
print(alphabetList)
counts = 0
def backTracking(parm) :
    global counts
    for vis in visited :
        for alpha in vis :
            if all( not alpha == 0 and alpL == alpha for alpL in alphabetList) :
                print ("all")
                return
            else : counts +=1


    cR, cC =  parm
    # print(cR,cC)
    for i in range(4) :
        nR = cR + dR[i]
        nC = cC + dC[i]
        if  not (nR < 0 or nC < 0 or nR >= R or nC >= C) and visited[nR][nC] == 0 :
            visited[nR][nC] = graph[nR][nC]
            backTracking((nR,nC))
            visited[nR][nC] = 0
        else :
            return

backTracking((0, 0))
print(counts)



