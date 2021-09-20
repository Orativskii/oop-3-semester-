import math
a = float(input("a="))
b = float(input("b="))
c = float(input("c="))
max = max((a+b+c),(a*b*c))
min = math.sqrt(min(((a+b+c)/2),(a*b*c))+1)
print("min" , (min))
print("max ", (max))