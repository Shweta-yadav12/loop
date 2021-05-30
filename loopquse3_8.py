# Courses
# Login/Signup
# Question 8

#     Ab hum pichli wali game ko thoda change karenge. Humne sirf yeh check kara the 
#     ki kya user ne jo number input kiya hai wo humare number ke barabar hai ya nahi.
#     Ab hum user ko yeh bhi batayenge ki jo usne number guess kiya hai, woh humare number se chota
#      hai ya bada hai. Jaise, agar user ne 4 input kiya. Hum check karenge ki kya 4 5 se 
#      chota hai?  Haan 4 5 se chota hai. Hum print karenge ki "aapka number chota hai!
#       Ek aur baar try karo".Phir hum user se ek baar aur number input lenge. Socho iss baar 
#       user ne 7 daala. Ab hum check karenge ki kya 7 5 se chota hai. Iska jawab nahi 
#       hoga. Ab hum print karenge ki "aapka number bada hai! Ek aur baar try karo".
#     Ab socho user ne 5 input kar diya. Yeh number humare number ke barabar ho jayega.
#      Ab hum print karenge ki " waah! Aapne number guess kar liya".
#     Hum aisa tab tak karte rahenge jab tak user humara number guess nahi kar leta. Ya
#      uski chances (jo ki 10 hain) khatam nahi ho jaati.

# User ko aise hint denge toh user ke liye guess karna asaaan ho jayega.
# Edit on Github


# i=1
# y=25
# while i<=5:
#     num=int(input("enter the number"))
#     if num==6:
#         print("congratulation you no is equal & gassing right")
#         break
#     elif num=<4:
#         print("Try Again")
#         # i=i+1
#     elif y<num:
#         print("gessing is high")
#     else:
#         print("gessing is high")
#         i=i+1
#         print("you not to able for gessing")
        



i=1
while i<=10:
    num=int(input("enter the number"))
    if num==4:
        print(num,"wha!,you are guessing number")
        break
    elif num<4:
        print(num,"your number small,so try again")
    elif num>4:
        print(num,"your number is big,so try again")
    i=i+1