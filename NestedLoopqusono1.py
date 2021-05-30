# Pattern question No1

a=1
i=1
while i<=4:
    b=1
    while b<=4-i:
        print(" ",end="")
        b=b+1
    j=1
    while j<=a:
        print("*",end="")
        j=j+1
    a+=2
    print()
    i=i+1