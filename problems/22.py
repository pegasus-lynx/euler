import csv
from common.paths import get_data_path
from maths.utils import word_to_num


DATA_FILE = get_data_path("0022_names.txt")
with DATA_FILE.open(encoding="utf-8", newline="") as file:
	names = next(csv.reader(file))


names.sort()
nums = [word_to_num(x) for x in names]
ans = 0

for ix, x in enumerate(nums):
    ans += (ix+1)*x

print(ans)
