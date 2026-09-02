from pathlib import Path
from common.paths import get_data_path


DATA_FILE = get_data_path("0081_matrix.txt")


def load_matrix(path: Path = DATA_FILE) -> list[list[int]]:
	with path.open(encoding="utf-8") as file:
		matrix = [list(map(int, line.strip().split(","))) for line in file if line.strip()]

	if len(matrix) != 80 or any(len(row) != 80 for row in matrix):
		raise ValueError(f"Expected an 80 by 80 matrix in {path}")

	return matrix


matrix = load_matrix()
print(matrix)

dp_matrix = matrix.copy()
n = 80
for i in range(1,80):
	dp_matrix[0][i] = dp_matrix[0][i-1] + matrix[0][i]
	dp_matrix[i][0] = dp_matrix[i-1][0] + matrix[i][0]

for i in range(1,80):
	for j in range(1,80):
		dp_matrix[i][j] = min(dp_matrix[i-1][j], dp_matrix[i][j-1]) + matrix[i][j]

print(dp_matrix[79][79])