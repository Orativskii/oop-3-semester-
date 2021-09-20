a = float(input("a="))
b = int(input("b="))
c = float(input("c="))
d = float(input("d="))
if a >= 0:
    if b > 0:
        s = a%b
        if s == c:
            print("raven c")
        if s == d:
            print("raven d")
else:
    print("end")