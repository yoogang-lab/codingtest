import sys
input = sys.stdin.readline

N, M, L = map(int, input().split())
list = [0] + list(map(int, input().split())) + [L]
list.sort() # list sort정렬

print(list)

start = list[0]
end = list[-1]

answer = end

while(start <= end) :
    mid = (start + end) // 2

    needed = 0

    for i in range(1, len(list)) :
        gap = list[i] - list[i - 1]
        if gap > mid :
            needed += (gap - 1) // mid
    if needed > M :
        start = mid + 1
    else :
        answer = mid
        end = mid - 1

print(answer)





