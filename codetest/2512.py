import sys
from bisect import bisect_left, bisect_right
sol = 0
input = sys.stdin.readline
n = int(input())
list = list(map(int, input().split()))
upperMax = int(input())
lo = 1
hi = max(list)

def is_possible(mid) :
    return sum(min(r, mid) for r in list) <=  upperMax

# mid = (lo + hi) // 2
while lo <= hi :
    mid = (lo + hi) // 2
    if is_possible(mid) :
        lo = mid + 1
        sol = mid
    else :
        hi = mid  - 1

print(sol)

# print( n, list, upperMax, findUpperValue)