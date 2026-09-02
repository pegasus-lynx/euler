from fractions import Fraction

N = 50

rts = N*N*3

for x1 in range(1, N+1):
    for y1 in range(1, N+1):
        slope = Fraction(y1, x1)
        inv_slope = -1 * (slope ** -1)
        dy = inv_slope.numerator
        dx = inv_slope.denominator
        for i in range(1,N+1):
            y2 = y1 + (i*dy)
            x2 = x1 + (i*dx)
            if x2 < 0 or x2 > N or y2 < 0 or y2 > N:
                break
            rts += 1
        for i in range(1,N+1):
            y2 = y1 - (i*dy)
            x2 = x1 - (i*dx)
            if x2 < 0 or x2 > N or y2 < 0 or y2 > N:
                break
            rts += 1

print(rts)