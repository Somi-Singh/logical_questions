def max():
    if num1>num2:
        print(num1,"is max")
    elif num2>num3:
        print(num2,"is max")
    elif num1==num2 and num2==num3:
        print(" All are equal")
    else:
        print(num3,"is max")
num1=int(input("enter the no="))
num2=int(input("enter the no="))
num3=int(input("enter the no="))
max()