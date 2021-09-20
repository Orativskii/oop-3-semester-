import math
katet1 = int(input('Катет 1 '))
katet2 = int(input('Катет 2 '))

print('Гіпотенуза', math.hypot(katet1, katet2))
print('Площа', 1/2 * katet1 * katet2)
