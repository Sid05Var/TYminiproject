import os
import math
import random
import smtplib



random_generator="0123456789"
# initializing the opt string

otp=""

for i in range(6):
    otp+=random_generator[math.floor(random.random()*10)]

# print("The otp generated is ",otp)

# static password of the user





print(otp)
    

# sending the opt through email and verifing the credentials
login='sidvarangaonkar5@gmail.com'
# passw=os.environ.get("Email_PASSWORD")
s = smtplib.SMTP('smtp.gmail.com',587)
s.starttls()
# login 1st parameter senders id second parameter reciver id

s.login(login,'ankfsvzxxgriyjyr')

# creating a dictionary of login and password



credentials=[{"id":"1032201708@mitwpu.edu.in","password":"sidd"},{"id":"1032201773@mitwpu.edu.in","password":"vaish"}]

emailid = input("Enter your email:- ")
s.sendmail('&&&&&&&&&&&',emailid,otp)

# verification
for i in credentials:
    if(i['id']==emailid):
        static_password2=i['password']
        

a = input("Enter Your embedded password :- ")



if a == (static_password2[0:2]+otp+static_password2[2:]):
    print("Verified")
    s.sendmail('&&&&&&&&&&&',emailid,"Thank you you had successfully loged in")
else:
    print("Please Check your OTP again")

    

