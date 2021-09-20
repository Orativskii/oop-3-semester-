n = input('n ')
array = list(map(int, n))
n = int(n)

if n <= 100:
    print(len(array), ' цифр')
    print(sum(array), ' сума цифр')
    print(array[len(array) - 1], ' последняя цифра')
    if n >= 10:
        print(array[len(array) - 2], ' предпоследняя цифра')



