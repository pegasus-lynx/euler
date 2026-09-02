from pathlib import Path
import copy
from common.paths import get_data_path

DATA_FILE = get_data_path("0067_triangle.txt")


def load_pyramid(file_path=DATA_FILE):
	"""Load the pyramid data as a list of integer rows."""
	with Path(file_path).open(encoding="utf-8") as triangle_file:
		return [list(map(int, line.split())) for line in triangle_file if line.strip()]


pyramid = load_pyramid()

dp_pyramid = copy.deepcopy(pyramid)

for i in range(1,len(pyramid)):
    dp_pyramid[i][0] += dp_pyramid[i-1][0]
    dp_pyramid[i][-1] += dp_pyramid[i-1][-1]

for i in range(2, len(pyramid)):
    for j in range(1, len(pyramid[i])-1):
        dp_pyramid[i][j] += max(dp_pyramid[i-1][j-1], dp_pyramid[i-1][j])

print(max(dp_pyramid[-1]))