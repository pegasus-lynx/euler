from maths.utils import get_digits

sqs = []
sqs_end = dict()
sqs_end[1] = 1
sqs_end[89] = 89

for i in range(0,10):
    sqs.append(i*i)

def get_sqs_end(x):
    if x in sqs_end:
        return sqs_end[x]
    digs = get_digits(x)
    sqs_sum = sum([sqs[d] for d in digs])
    sqs_end[x] = get_sqs_end(sqs_sum)
    return sqs_end[x]

cnt = 0
for p in range(1,10000000):
    end = get_sqs_end(p)
    if end == 89:
        cnt += 1

print(cnt)