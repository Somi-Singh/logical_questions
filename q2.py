sold=int(input("enter any soldiers="))
l=[]
i=1
even_c=0
odd_c=0
while i<=sold:
    weapo=int(input("enter any number of weapons="))
    l.append(weapo)
    if l[i]%2!=0:
        odd_c+=1
    else:
        even_c+=1
    i+=1
if even_c<odd_c:
    print("not ready")
elif even_c>odd_c:
    print("ready for battle")
else:
    print("not ready")








    
