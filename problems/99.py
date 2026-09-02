from math import log2
from common.paths import get_data_path

data_file = get_data_path("0099_base_exp.txt")

with data_file.open(encoding="utf-8") as file:
	base_exponent_pairs = [tuple(map(int, line.split(","))) for line in file if line.strip()]

vals = []

for base, exp in base_exponent_pairs:
	vals.append(exp*log2(base))

maxval = max(vals)

for i,v in enumerate(vals):
	if maxval == v:
		print(i+1)
		break