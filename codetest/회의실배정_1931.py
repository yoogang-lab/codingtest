#https://www.acmicpc.net/problem/1931

import sys
from copy import deepcopy

input = sys.stdin.readline

N = int(input())
timeList = list(list(map(int, input().split())) for _ in range(N))
# print(timeList)
# dd = deepcopy(timeList)
timeList.sort(key=lambda x: (x[1], x[0]))

# print(dd)
count = 1
endTime = timeList[0][1]
for i in range(1, N) :
    a,b = timeList[i]
    if a >= endTime :
        # print(a, b)
        endTime = b
        count +=1

print(count)




