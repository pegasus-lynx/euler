
word_lens = {
    1: 3,
    2: 3,
    3: 5,
    4: 4,
    5: 4,
    6: 3,
    7: 5,
    8: 5,
    9: 4,
    10: 3,
    11: 6,
    12: 6,
    13: 8,
    14: 8,
    15: 7,
    16: 7,
    17: 9,
    18: 8,
    19: 8,
    20: 6,
    30: 6, #thirty
    40: 5, #forty
    50: 5, #fifty
    60: 5, #sixty
    70: 7, #seventy
    80: 6, #eighty
    90: 6, #ninety
    100: 7, #hundred
    1000: 8
}

sum_1_9 = 0
sum_1_19 = 0
sum_1_99 = 0
sum_1_999 = 0

for x in range(1,10):
    sum_1_9 += word_lens[x]

for x in range(1,20):
    sum_1_19 += word_lens[x]

sum_1_99 = sum_1_19
for x in range(20,100,10):
    sum_1_99 += 10*word_lens[x]
    sum_1_99 += sum_1_9

sum_1_999 = sum_1_99
for x in range(100,1000,100):
    sum_1_999 += sum_1_99
    sum_1_999 += (word_lens[x//100] + word_lens[100] + 3) * 100  ## 3 = and
    sum_1_999 -= 3


ans = sum_1_999 + word_lens[1] + word_lens[1000]
print(ans)