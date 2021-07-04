def factorial():
    i=1
    factorial=1
    while i<=num:
        factorial=factorial*i
        i=i+1
    print(factorial)
num=int(input('Enter Your Number='))
factorial()