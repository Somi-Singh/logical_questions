num=int(input("enter number"))
i=0
while i<=num:
    j=1
    c=0
    while j<=i:
        if i%j==0:
            c+=1
        j+=1
    if c==2:
        print(i)
    i+=1
