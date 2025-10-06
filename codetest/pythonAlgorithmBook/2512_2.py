N = int(input())
arr = list(map(int, input().split()))
target = int(input())

# print(N, arr, target)

start = 1
# end = 1000000000
result = 0

arr.sort()
end = arr[-1]
# print(arr)


def checkSanghan(sangHan) :
    sum = 0
    for value in arr :
       if value >= sangHan :
           sum += sangHan
       else :
           sum += value
    return sum

while (start <= end) :
    mid = (start + end) // 2

    if target >= checkSanghan(mid) :
        start = mid + 1
        result = mid
    else :
        end = mid - 1


print(result)

