# Courses
# Login/Signup
# Question 4

# Code likho jisse 30 se 420 tak ke unn numbers ka sum calculate ho jo 8 ke multiple hai 
# yaani wo numbers 8 ke table (paahade) mein aate hai.

sum=0
i=30
while i<=420:
    if i%8==0:
        sum=sum+i
    i+=1
print(sum)
