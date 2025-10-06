import sys
input = sys.stdin.readline
data = []
C, N = map(int, input().split())

cities = [tuple(map(int, input().split())) for _ in range(N)]

# print(data)
max_customer = max(city[1] for city in cities) #가지고 있는 고객 값 중 제일 큰것으로 대체
print(max_customer)
INF = 10**9
dp = [INF] * (C + max_customer + 1)
dp[0] = 0

for cost, customer in cities:  # list여도 언패킹 가능
    for i in range(customer, C + max_customer + 1):
        dp[i] = min(dp[i], dp[i - customer] + cost)
        print(i, dp[i])

answer =dp[C]
print(answer)