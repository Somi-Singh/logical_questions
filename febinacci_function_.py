# function of febonchi number#
#1
def fbnc(num):
    i=1
    sum_i=0
    a=0
    while i <=num:
        print(a,end=" ")
        sum_i=i
        i=a
        a=a+sum_i
fbnc(10)



#2
def fbnc(num):
    i,b=1,0
    sum_i=0
    a=0
    while i <=num:
        print(i)
        b,i=i,i+b
fbnc(10)

def fbnc(num):
    i=1
    sum_i=0
    a=0
    empty=[]
    while i <=num:
        empty.append(a)#2
def fbnc(num):
    i,b=1,0
    sum_i=0
    a=0
    while i <=num:
        print(i)
        b,i=i,i+b
fbnc(10)

def fbnc(num):
    i=1
    sum_i=0
    a=0
    empty=[]
    while i <=num:
        empty.append(a)
        sum_i=i
        i=a
        a=a+sum_i
    return(empty)
a=fbnc(10)
print(a)




       
        