def frequency(list1):
    i=0
    empty={}
    while i<len(list1):
        j=0
        count=0
        while j<len(list1):
            if list1[i]==list1[j]:
                count=count+1
            j=j+1
        empty[list1[i]]=count
        i=i+1
    print(empty)
list1=[1,1,1,2,2,3,4,4,5]
frequency(list1)