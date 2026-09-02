from common.paths import get_data_path

data_path = get_data_path("0102_triangles.txt")

with data_path.open(encoding="utf-8") as data_file:
	triangles = [list(map(int, line.strip().split(","))) for line in data_file if line.strip()]

def get_triangle_area(x1,y1,x2,y2,x3,y3):
	area = 0
	area += x1*(y2-y3)
	area += x2*(y3-y1)
	area += x3*(y1-y2)
	area = area / 2
	return abs(area)

cnt = 0
for t in triangles:
    area = get_triangle_area(t[0], t[1], t[2], t[3], t[4], t[5])
    area1 = get_triangle_area(0, 0, t[2], t[3], t[4], t[5])
    area2 = get_triangle_area(t[0], t[1], 0, 0, t[4], t[5])
    area3 = get_triangle_area(t[0], t[1], t[2], t[3], 0, 0)
    if area == (area1+area2+area3):
        cnt += 1

print(cnt)