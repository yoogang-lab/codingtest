import sys
input = sys.stdin.readline

# 5 3
# 1
# 2
# 8
# 4
# 9

N, C = map(int, input().split())
# print(N, C)

location = list(int(input()) for _ in range(N))
# print(location)

location.sort()

# print(location)

start = 0
end = 1000000000

result = 0

#
# def checkDistance(value):
#     for i in range(N):
#        value2 =  location[i] + value
#        if abs(value2 - location[i])
#             # if (abs(location[i] - location[j]) == value):
#             #     return True
#     # return False
#
#


while (start <= end) :
    mid = (start + end) // 2

    count = 1
    current = location[0]
    for i in range(1, N):
        if abs(location[i] - current) >= mid:
            current = location[i]
            count += 1

    if count >= C :
        start = mid + 1
        result = mid
    else :
        end = mid - 1


print(result)




