
p = 1
q = 10

cubes = []
x = 1
while True:
    xcube = pow(x,3)
    if xcube < q:
        cubes.append(xcube)
        x += 1
        continue
    cubes_dict = dict()
    for cb in cubes:
        scb = ''.join(sorted(str(cb)))
        if scb not in cubes_dict:
            cubes_dict[scb] = []
        cubes_dict[scb].append(cb)
    found = False
    for k,v in cubes_dict.items():
        if len(v) == 5:
            found = True
            print(v[0])
            break
    if found:
        break
    p *= 10
    q *= 10
    cubes = []