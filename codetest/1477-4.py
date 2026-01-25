import sys
input = sys.stdin.readline

N , M , L = map(int, input().split())
list = list(map(int, input().split()))
# print(N,M,L)
# print(list)
list +=[0, L]
list.sort()

left = list[0]
right = list[-1]

sol = 0
while left <= right :
    mid = (left + right) // 2
    needed = 0

    for i in range(1, len(list)) :
       gap = (list[i] - list[i - 1])
       if gap >= mid :
            needed += (gap - 1) // mid

    # print(needed)
    if needed > M :
        left = mid + 1

    else :
        sol = mid
        right = mid - 1


print(sol)


