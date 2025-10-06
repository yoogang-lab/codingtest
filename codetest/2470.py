from xmlrpc.client import MAXINT

N = int(input())
arr = list(map(int,input().split()))
arr.sort()
# print(arr)

start = 0
end = N - 1
result = 0
min_val = float('inf')
answer=[0,1]

while start < end :
   ans = arr[start] + arr[end]

   if min_val > abs(ans) :
       min_val = abs(ans)
       answer[0] = start
       answer[1] = end

   if ans < 0 :
        start = start + 1
   elif ans > 0 :
       end = end - 1
   else :
       break

print(arr[answer[0]], arr[answer[1]])