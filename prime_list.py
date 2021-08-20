#Who is Prime no in this list-
#Slove by using append


a=[10,7,3,6,77,45]
i=0
b=[]
while  i<len(a):
	j=1
	fac=0
	while j<=a[i]:
		if a[i]%j==0:
			fac=fac+1
		j=j+1
	if fac==2:
		b.append(a[i])
	i+=1
print(b)