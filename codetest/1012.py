import sys
sys.setrecursionlimit(10000)

def dfs(node, graph, M, N):
    cx, cy = node
    graph[cx][cy] = 2

    for i in range(4):
        nx = cx + dx[i]
        ny = cy + dy[i]
        if nx >= 0 and nx < N and ny >= 0 and ny < M :
            if graph[nx][ny] == 1 :
                dfs((nx, ny), graph, M, N)

T = int(input()) #Test case 갯수

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

#graph 순회 하면서 1을 찾고 dfs 탐색으로 2로 바꿔놓음.
# 순회가 끝나면 다시 1을 찾고 모든 탐색이 끝나면 종료


for t1 in range(T):
    count = 0
    M, N, K = map(int, input().split())
    graph = [[0] * (M) for _ in range(N)]
    # print(graph)
    # print(graph[9][4])
    for _ in range(K):
        x, y = map(int, input().split())
        # print(x, y)
        graph[y][x] = 1

    # print("t1 ", t1)
    for i in range(N):
        for j in range(M):
            # print(i, j)
            if graph[i][j] == 1:
                count += 1
                dfs((i, j), graph, M, N)
    print(count)
    # print(graph)
# print(count)





