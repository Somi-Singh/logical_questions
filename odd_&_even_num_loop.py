# odd and even number#
num=int(input("enter number"))
for i in range(2,num):
    if i%2==0:
        print("even",i)
        continue
    else:
        print("odd",i)
