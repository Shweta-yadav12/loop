# Courses
# Login/Signup
# Question 6
# Question 6

# Prime numbers woh numbers hote hai jo sirf 1 aur apne aap se divisible hote hain.
#  Jaise 1. 13 prime hai kyunki 13 sirf 13 aur 1 se perfectly divide hota hai. Aur kisi bhi number 
#  se perfectly divide nahi hota. 2. 4 prime nahi hai kyunki 4 apne aap se aur 2 aur 1 se perfectly 
 
# divide hota hai.
# Prime number ke liye aapko check karna hoga ki woh number kaun kaun se numbers se divisible hai. 
# Yeh loop chala ke kar sakte ho.

num=int(input("enter the number"))
factor=0
i=1
j=num
while i<=j:
    if (j%1==0):
        print("factor",i)
        factor=factor+1
    i=i+1
if factor==2:
    print("prime number",num)
    
else:
    print("not prime number",num)