import csv
from common.paths import get_data_path
from maths.utils import word_to_num

DATA_FILE = get_data_path("0042_words.txt")
with DATA_FILE.open(encoding="utf-8", newline="") as file:
	names = next(csv.reader(file))


triangle_words = 0
triangle_nums = set([(x*(x+1))//2 for x in range(1, 101)])
tnums = set()
for name in names:
	num = word_to_num(name)
	tnums.add(num)
	if num in triangle_nums:
		triangle_words += 1

print(triangle_words)
	