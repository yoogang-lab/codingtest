N = int(input())
listN = list(map(int, input().split()))
M = int(input())
listM = list(map(int, input().split()))
# print(listN)

#값 찾을 리스트 정렬(이분 탐색)
listN.sort()
# print(listN)

def binarySearch(target, findList, start, end) :
    if start > end:  # start와 end 커서가 역전 되면 값이 없는것
        return -1

    mid = (start + end) // 2  # 중간값

    if findList[mid] == target:  # 중간값의 데이터가 target과 같다면 mid를 반환
        return mid
    elif findList[mid] > target:  # target이 mid값보다 작으면 mid의 left 검색
        end = mid - 1
    else:  # target이 mid 값보다 크면 right로 탐색
        start = mid + 1

    return binarySearch(target, findList, start, end)  # 재귀로 -1이나 mid가 리턴 될때까지 계산

for item in listM:
    if binarySearch(item, listN, 0, N - 1) != -1 :
        print(1)
    else:
        print(0)

