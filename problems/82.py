from pathlib import Path
from common.paths import get_data_path
import heapq
import copy


DATA_FILE = get_data_path("0082_matrix.txt")


def load_matrix(path: Path = DATA_FILE) -> list[list[int]]:
	with path.open(encoding="utf-8") as file:
		matrix = [list(map(int, line.strip().split(","))) for line in file if line.strip()]

	# if len(matrix) != 80 or any(len(row) != 80 for row in matrix):
	# 	raise ValueError(f"Expected an 80 by 80 matrix in {path}")

	return matrix


matrix = load_matrix()
total_sum = sum([sum(x) for x in matrix])

dxs = [0,-1,1]
dys = [1,0,0]

n = 80
dp = copy.deepcopy(matrix)
for i in range(n):
    for j in range(1,n):
        dp[i][j] = total_sum

pq = []
for i in range(n):
    heapq.heappush(pq, (dp[i][0], i, 0))

while pq:
    val, x, y = pq[0]
    heapq.heappop(pq)

    for dx,dy in zip(dxs,dys):
        nx = x+dx
        ny = y+dy

        if nx < 0 or nx >= n or ny < 0 or ny >= n:
            continue

        nval = dp[x][y] + matrix[nx][ny]
        if nval < dp[nx][ny]:
              dp[nx][ny] = nval
              heapq.heappush(pq, (nval, nx, ny))

print(min([dp[i][n-1] for i in range(n)]))