import sys
input = sys.stdin.readline

N = int(input())
K = int(input())

# print(N, K)

left = 1
right = N * N

answer = 0

while left <= right :
    mid = (left + right) // 2

    belowCnt = 0
    for num in range(1, N + 1) :
        belowCnt+= min(N, mid//num) #행에서 작은값은 몇개인가 줄마다 mid보다 작은게 몇개냐
        # “어떤 값 X보다 작거나 같은 수는 몇 개냐?”

    if belowCnt >= K :
        answer = mid
        right = mid - 1
    else :
        left = mid + 1

print(answer)