
def is_palindrome(num):
    nstr = str(num)
    rnstr = nstr[::-1]
    return nstr == rnstr

ans = 0

for x in range(100,999):
    for y in range(x,999):
        z = x*y
        if(is_palindrome(z)):
            if z > ans:
                ans = z

print(ans)