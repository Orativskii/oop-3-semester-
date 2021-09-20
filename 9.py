import math

r1 = int(input('r1 '))
r2 = int(input('r2 '))
r3 = int(input('r3 '))

r = (r1 * r2 * r3)/(r1 * r2 + r2 * r3 + r1 * r3)

print('R = ', r)