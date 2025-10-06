N, M = map(int, input().split())
arr = [int(input()) for _ in range(N)]

arr.sort()
# print(arr)

start = 1
end = arr[-1] - arr[0] #끝에서 부터 자른다면
# candidate = set()
# s = {1, 2, 3}
# result
# result = 0
# for i in range(0, N):
#     print(i)

while (start <= end) :
    mid = (start + end) // 2 # <- 최대거리
    # candidate = set()
    # print("mid === ", mid)
    current = arr[0]
    count = 1
    for i in range(1, N) :
        if (abs(arr[i] - current)  >= mid) :
            current = arr[i]
            count += 1


    # print("len ==== ", count)
    if count >= M :
        start = mid + 1
        result = mid
    else :
        end = mid - 1

print( result)




