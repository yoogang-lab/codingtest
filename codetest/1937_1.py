from collections import deque
import sys

sys.setrecursionlimit(10 ** 6)

N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]

# 상, 하, 좌, 우 이동 방향
dR = [0, 0, -1, 1]
dC = [1, -1, 0, 0]

# DP 테이블 초기화: -1은 아직 계산되지 않은 상태를 의미
DP = [[-1] * N for _ in range(N)]


def dfs(r, c):
    # 이미 계산된 셀은 바로 반환
    if DP[r][c] != -1:
        return DP[r][c]

    # 자기 자신만으로도 길이는 1
    DP[r][c] = 1

    for i in range(4):
        nr, nc = r + dR[i], c + dC[i]
        # 범위 내이고, 다음 셀의 값이 현재 셀보다 큰 경우
        if 0 <= nr < N and 0 <= nc < N and graph[nr][nc] > graph[r][c]:
            DP[r][c] = max(DP[r][c], 1 + dfs(nr, nc))

    return DP[r][c]


maxMoveCnt = 0  # 전체에서 최대 경로 길이 저장

# 모든 셀에 대해 DFS 수행
for i in range(N):
    for j in range(N):
        maxMoveCnt = max(maxMoveCnt, dfs(i, j))

print(maxMoveCnt)