
yer=int(input("enter the yer"))
if yer%4==0:
    if yer%100==0:
        if yer%400==0:
            print("it is leaps year")
        else:
            print("it is not centar year")
    else:
        print("it is leaps year")
else:
    print("it is not leaps ")
