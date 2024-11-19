a, b = int(input("enter a value: ")), int(input("enter a value: "))
x,y = a, b
while a != 0 and b != 0:
    if a > b:
        a = a%b
    elif b > a:
        b = b%a
if a==0:
    print("GCD = ", b)
    print("LCM is = ", (x*y)/b)
else:
    print("GCD = ", a)
    print("LCM = ", (x*y)/a)
