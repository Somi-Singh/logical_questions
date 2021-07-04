def campus_name():
    i=1
    while i<=1000:
        if i%3==0:
            print("Nav")
        elif i%7==0:
            print("gurukul")
        elif i%21==0:
            print("Navgurukul")
        else:
            print(i)
        i=i+1
campus_name()