n= int(input())
v= int(input())
graph = [[] for _ in range( n + 1)]
for _ in range(v):
	n1, n2 = map(int, input().split())
	graph[n1].append(n2)
	graph[n2].append(n1) # 양방향 그래프인 경우

visited = [False] * (n + 1)
count = 0
def dfs(start) :
    global count
    visited[start] = True
    # # print(count)
    # nx = graph[start].pop()
    # print(nx)
    for nx in graph[start] :
        if not visited[nx] :
            count += 1
            dfs(nx)
    else :
        return

dfs(1)
print(count)