
from maths.utils import get_digits

for num in range(11,99):
    for den in range(num+1,100):
        if num % 10 == 0 and den % 10 == 0:
            continue

        nd = get_digits(num)
        dd = get_digits(den)

        if nd[0] == dd[0] or nd[1] == dd[1]:
            continue
        
        if nd[1] == dd[0] or nd[1] == dd[1]:
            new_num = nd[0]
            new_den = dd[1]

            if new_num * den == num * new_den:
                print(num, den)
                print(new_num, new_den)