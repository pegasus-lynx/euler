

seqs = set()

for a in range(2,101):
    for b in range(2,101):
        seqs.add(pow(a,b))

print(len(seqs))