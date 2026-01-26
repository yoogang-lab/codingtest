import sys
input = sys.stdin.readline

N, C = map(int, input().split())
list = list(int(input()) for _ in range(N))
list.sort()
# print(list)

left = 1
right = list[-1] - list[0]

# for index in range(0, len(list)):
#     print(index)
sol = 0
while left <= right :
    mid = (left + right) // 2
    setGong = 1
    # print('mid', mid)

    last = list[0]

    for i in range(1, N) :
        if list[i] - last >= mid :
            setGong += 1
            last = list[i]

    if setGong >= C :  #
        sol = mid
        left = mid + 1

    else :
        right = mid - 1

print(sol)
