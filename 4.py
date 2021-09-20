import numpy as np
x = float(input("x="))
y = float(input("y="))
if x < 0:
    print('net')
if y < 0:
    print('net')
print((x+y)/2)
u = np.exp(np.mean(np.log([x, y])))
print(u)