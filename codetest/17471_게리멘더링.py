# # https://www.acmicpc.net/problem/17471
# # 1. 조합 구한다. 2개를 뽑는다.
# import sys
# from collections import deque
# from itertools import combinations
# input = sys.stdin.readline
#
# #
# # 6
# # 5 2 3 4 1 2
#
# # 2 2 4 2개 2-4
# # 4 1 3 6 5
# # 2 4 2
# # 2 1 3
# # 1 2
# # 1 2
#
# N = int(input())
# peopleCntList = list(map(int, input().split()))
#
# # print(N)
# # print(peopleCntList)
#
# mapListInput = list(list(map(int, input().split())) for _ in range(N))
# mapList = []
# #
# # print(mapList)
# # print(mapListInput)
#
# for i in range(N) :
#     mapList.append([] * mapListInput[i][0])
#     for j in range(mapListInput[i][0]) :
#         mapList[i].append(mapListInput[i][j+1])
#
# print(mapList)
# pointList = []
# for i in range(N) :
#     pointList.append(i + 1)
#
# pointListComb = []
# r = 3
#
# def combination(start, path, result, r) :
#     if (len(path) == r) :
#         result.append(path[:])
#         return result
#
#     for i in range(start, N) :
#         path.append(pointList[i])
#         combination(i + 1, path, result, r)
#         path.pop()
#     return result
#
#
# print()
# # print(result)
# for i in range(1, N) :
#     pointListComb.extend(combination(0, [], [], i))
#
#
#
# groupA = []
# groupB = []
#
# # 서로 안 겹치는 조합 쌍 찾기
# for item in pointListComb:
#     for item2 in pointListComb:
#         if item is item2:
#             continue
#
#         # 두 조합이 완전히 겹치지 않는지 확인
#         disjoint = True
#         for x in item:
#             if x in item2:
#                 disjoint = False
#                 break
#
#         if disjoint:
#             groupA.append(item)
#             groupB.append(item2)
#             # print("A =", item, " / B =", item2)
#
# # for item in pointListComb :
# #     groupA.append(item)
# #     print("groupA item ", groupA)
# #     for item2 in pointListComb:
# #         print("item2 ", item2)
# #         if not item[0] in item2 :
# #             print("item : ", item)
# #             groupB.append(item2)
#
# print("groupA: ", groupA)
# print("groupB: ", groupB)
#
#
#
# # for a in pointListComb :
# #     # print("Dfsa1 ", a[0])
# #     for zeroA in a :
# #         print("groupA ", zeroA)
# #         for b in pointListComb :
# #             # print(not a in b)
# #             for zeroB in b :
# #                 print("zeroB ", zeroB)
# #                 if not zeroA in zeroB :
# #                     print("groupB " , zeroA)
#
#
# print (pointListComb)
#
# def bfs(area) :
#     queue = deque()
#     queue.append(area[0])
#     visited = []
#     visited.append(area[0])
#
#     while(queue) :
#         cur = queue.popleft()
#         for next2 in mapList[cur] :
#             if not next2 in visited :
#                 queue.append(next2)
#                 visited.append(next2)
#
#     return len(visited) == len(area)
#
# if bfs(groupA) and bfs(groupB) :
#
#
#
#
#     # for
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
