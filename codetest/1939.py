from collections import deque
import sys

N, M = map(int, input().split())
arr = list(list(map(int, input().split())) for _ in range(M))
factory1, factory2 = map(int, input().split())

# print(N, M)
# print(arr)
# print(factory1, factory2)
arr.sort(key=lambda x: x[2])

# print(arr)
start = 1
end = 1000000000

#dfs로 길찾기
# def dfs(A, D) :
#     ar
# G = [[]]
# graph = [[] for _ in range(M + 1)]
# print(graph)
# for i in range(0, M) :
#     print(arr[i][0])
#     graph[arr[i][0]].append(arr[i][1])
#     graph[arr[i][1]].append(arr[i][0])
# print(graph)
result = 0
#
# def dfs (f1, f2, graph,visited) :
#     visited[f1] = True
#     if f2 == f1 :
#         return True
#
#     for index in graph[f1] :
#         if not visited[index] :
#             if dfs(index, f2, graph, visited) :
#                 return True
#     return False

#
graph = [[] for _ in range(N + 1)]
for i in range(M):
    graph[arr[i][0]].append((arr[i][1],arr[i][2]))
    graph[arr[i][1]].append((arr[i][0],arr[i][2]))

def bfs(weight, graph, start) :


    visited = list([False] * (N + 1) )
    queue = deque([start])
    visited[start] = True

    while queue :
        current = queue.popleft()
        if (current == factory2)  :
            return True
        for next, value in graph[current] :
            # print("current" , graph[i])
            if (not visited[next] and value >= weight) :
                queue.append(next)
                visited[next] = True

    return False







while start <= end :
    mid = ( end + start) // 2
    # 무게가 많아서 갈 수 없는 경우는 end = mid -1
    # 무게가 적어서 갈 수 있는 경우는 start= mid + 1

    # print("graph ", graph)
    # for i in range(M):
    #     graph[arr[i][0]][arr[i][1]] = arr[i][2]
    #     graph[arr[i][1]][arr[i][0]] = arr[i][2]
    #         # visited[arr[i][0]].append(False)
            # visited[arr[i][1]].append(False)
    # print("graph ", graph)
    #
    # if len(visited) >= 2 :
    #     visited[factory1] = True
    #     findPath = dfs(factory1, factory2, graph, visited)
    #     print(findPath)
    # else :
    #     findPath = False
    # print("mid", mid)
    # findPath = bfs(mid, graph, visited, factory1);
    # print("fidPath", findPath)
    if bfs(mid, graph, factory1) :
        start = mid + 1
        result = mid
    else :
        end = mid - 1

print(result)