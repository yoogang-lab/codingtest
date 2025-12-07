import sys
import math
input = sys.stdin.readline

N, M = map(int, input().split())
listData = list(list(map(int, input().split())) for _ in range(M))
# print(listData)

# print(N, M)

# 1.0번째 인덱스 기준으로 정렬
# 2. 0번째 인덱스 는 6 묶음이다. N을 먼저 6으로 나눔
# 3. 1번째 인덱스 기준으로 정렬
# 4. 1번째 인덱스는 1개 기준이다.
sol = 0
sol2 = 0
sol3 = 0

listData.sort(key = lambda x : (x[0],x[1]))
# print(listData)
sixtas =N / 6
# print(sixtas)

if (sixtas > 0) :
    sol += listData[0][0] *  int(sixtas)
    sol2 += listData[0][0] * math.ceil(sixtas)



remain = (N - (int(sixtas) * 6)) % 6
# print(sol)
# print(N - (int(sixtas) * 6))
if (remain > 0) :
    listData.sort(key=lambda x: (x[1], x[0]))
    # print(listData)
    # print(listData[0][1] )
    sol += listData[0][1] * remain


listData.sort(key=lambda x: (x[1], x[0]))
sol3 += listData[0][1] * N
#
# print(sol)
# print(sol2)

print(min(sol2, sol, sol3))


