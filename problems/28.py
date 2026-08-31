

diags = [1]
curr = 1
for sz in range(1,1000,2):
    for ix in range(4):
        curr += sz+1
        diags.append(curr)
print(sum(diags))