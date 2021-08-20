d={}
for i in  range(1):
    user1=input("enter the name :")
    user2=int(input("enter the age:"))
    dic={"name":user1,"age":user2}
    d.update(dic)
print(d)                                                                                                                                            
n=int(input("enter a number"))
i=1
a={}
a[i]=n
while i<=n:
    m=[]
    j=1
    while j<=10:
        pro=i*j
        m.append(pro)
        j+=1
    a[i]=m
    i+=1
print(a)                                                                                                                                  