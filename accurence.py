def occerenc():
    i=0
    empty=[]
    while i<len(my_list):
        j=0
        empty2=[]
        count=0
        while j<len(my_list):
            if my_list[i]==my_list[j]:
                count=count+1
            j=j+1
        empty2.append(my_list[i])
        empty2.append(count)
        if empty2 not in empty:
            empty.append(empty2)
        i=i+1
    print(empty)
my_list=[10,10,10,10,20,20,20,20,40,40,50,50,30]
occerenc()