

def get_digits(x, reversed_list = False):
    digits = []
    while x != 0:
        digits.append(x%10)
        x = x // 10
    if reversed_list:
        return digits

    digits.reverse()
    return digits

def digits_to_num(digits, reversed_list = False):
    x = 0
    if not reversed_list:
        digits.reverse()

    for i, d in enumerate(digits):
        x += d * pow(10,i)

    return x

def word_to_num(word):
    ret = 0
    word = word.upper()
    for c in word:
        ret += 1 + ord(c) - ord('A')
    return ret

def is_palindrome(x):
    digs = get_digits(x)
    p = 0
    q = len(digs)-1
    while p < q:
        if digs[p] != digs[q]:
            return False
        p += 1
        q -= 1
    return True