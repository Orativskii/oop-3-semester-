x = y = 0

while x == y:
    x = float(input('x '))
    y = float(input('y '))

if x > y:
    y = (x + y)/2
    x = x * y * 2
else: 
    x = (x + y)/2
    y = x * y * 2

print('x ', x,'y ', y)


