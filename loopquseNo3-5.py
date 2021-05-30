# Courses
# Login/Signup
# Question 5

# 11 logon ka weight input le aur fir average weight print kare. Aur fir yeh bhi check kare ki 
# kya Average weight 5 ka multiple (Yaani 5 se bhaag karne par shesh 0 bachta hai) hai ya nahi? 
# Note: Isme aapko input ka use karna padega. Aap loop ke andar raw input ka use kar ke 11 baar 
# raw_input le sakte ho


# i=1
# sum=0
# while i<=11:
#     x=int(input("enter the age"))
#     sum=sum+1
#     i=i+1
#     printe(sum)
    


i=1
average=0
while i<=100:
    if i<=1:
        x=int(input("enter the number"))
        average=average+1
    i=i+1
print(x*11)
if (x*11)/11:
    print((x*11)/11,"average")
    if ((x*11)/11)%5==0:
        print("divisibl hai")
    else:
        print("divisible nahi hai")    