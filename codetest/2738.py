
N, M = map(int, input().split())


matrixInputA = [list(map(int, input().split())) for _ in range(N)]
#
# for _ in range(M):
matrixInputB = [list(map(int, input().split())) for _ in range(N)]

# matrinxresult = [[0] * M for _ in range(N)]

# print(matrixInputA, matrixInputB)


matrixResult  = [[matrixInputA[i][j] + matrixInputB[i][j]  for j in range(M)] for i in range(N)]

for row in matrixResult :
    print(*row)

# for i in range(N) :
#     for j in range(M) :
#         print(matrixResult[i][j], end = " ")
#     print()