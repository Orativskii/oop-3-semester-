k = int(input('k '))
l = int(input('l '))

if k != l:
    maxValue = max(k, l)
    k = maxValue
    l = maxValue
else:
    k = 0
    l = 0