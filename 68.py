def palindrom(x, partial=0):
    if x == 0:
        return partial
    return palindrom(x // 10, partial * 10 + x % 10)

def equalNumber(n):
    if n.count(n[0]) == 3 or n.count(n[1]) == 3 or n.count(n[2]) == 3 or n.count(n[3]) == 3:
        print('Є три однакові цифри')

def notEqualNumber(n):
        if n.count(n[0]) == 1 and n.count(n[1]) == 1 and n.count(n[2]) == 1 and n.count(n[3]) == 1:
            print('Всі цифри різні')


n = int(input('n '))

array = list(map(int, str(n)))

if n <= 9999:
    if(palindrom(n) == n):
        print('Це паліндром')
    n = str(n)
    equalNumber(n)
    notEqualNumber(n)


