d={}
for i in  range(1):
    user1=input("enter the name :")
    user2=int(input("enter the age:"))
    dic={"name":user1,"age":user2}
    d.update(dic)
print(d)       