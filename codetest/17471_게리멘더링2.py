import sys
from collections import deque
from itertools import combinations
input = sys.stdin.readline

N = int(input())
people = list(map(int, input().split()))

adj = [[] for _ in range(N)]
for i in range(N):
    info = list(map(int, input().split()))
    for x in info[1:] :  # input의 1번 인덱스 부터 출력 해서
        print("x " , x)
        adj[i].append(x - 1)

print("kk ,", adj)

areas = [i for i in range(N)]

print("kk2 ", areas)

def bfs(group):
    start = group[0]
    q = deque([start])
    visited = set([start])
    print("visited sa ", visited)

    while q:
        cur = q.popleft()
        for nxt in adj[cur]:
            if nxt in group and nxt not in visited:
                visited.add(nxt)
                q.append(nxt)

    return len(visited) == len(group)


result = 1e9

for r in range(1, N):
    print("fdsadf r ", r, combinations(areas, r))
    for groupA in combinations(areas, r):

        groupB = list(set(areas) - set(groupA))

        # print("groupAA ", set(areas) )
        print("groupAA ", groupA)
        print("groupBB ",groupB )

        if bfs(groupA) and bfs(groupB):
            sumA = sum(people[i] for i in groupA)
            sumB = sum(people[i] for i in groupB)
            result = min(result, abs(sumA - sumB))

print(result if result != 1e9 else -1)