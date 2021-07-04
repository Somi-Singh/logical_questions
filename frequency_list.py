def frequency(list1):
    i=0
    empty=[]
    while i<len(list1):
        j=0
        count=0
        b=[]
        while j<len(list1):
            if list1[i] == list1[j]:
                count=count+1
            j=j+1
        b.append(list1[i])
        b.append(count)
        if b not in empty:
            empty.append(b)
        i=i+1
    print(empty)
list1=[1,1,1,2,2,3,4,4,5]
frequency(list1)