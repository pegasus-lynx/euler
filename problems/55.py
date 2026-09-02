from maths.utils import is_palindrome, get_digits, digits_to_num

lychrel = []

for x in range(1,10000):
    is_lychrel = True
    y = x + digits_to_num(get_digits(x, True))
    for i in range(50):
        if is_palindrome(y):
            is_lychrel = False
            break
        y = y + digits_to_num(get_digits(y, True))
    if is_lychrel:
        lychrel.append(x)

print(len(lychrel))