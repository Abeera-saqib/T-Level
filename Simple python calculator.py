while True:
    n1 = int(input("enter number 1 ="))
    n2 = int(input("enter number 2 = "))
    print("1.addition 2.subtraction 3.multiplication 4.division 5.module 6.exit")
    ch = int(input("enter your choice = "))
    if ch == 1:
        print("addition = ", n1+n2)
    if ch == 2:
        print("subtraction = ", n1-n2)
    if ch == 3:
        print("multiplication = ", n1*n2)
    if ch == 4:
        print("division = ", n1/n2)
    if ch == 5:
        print("module = ", n1%n2)
    elif ch == 6:
        break 
    else:
        print("enter a valid choice")
