import math

k = float(input('k '))
m = float(input('m '))

x = float(input('x '))
y = float(input('y '))
z = float(input('z '))

if k < math.pow(m, 2):
    x = abs(x)
    y -= 0.5
    z -= 0.5
elif k == math.pow(m,2):
    y = abs(y)
    x -= 0.5
    z -= 0.5
elif k > math.pow(m,2):
    z = abs(z)
    x -= 0.5
    y -= 0.5

print(x, y, z)



