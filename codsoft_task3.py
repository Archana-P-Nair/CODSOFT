import random as r
print("***********")
print("Welcome to Password Generator !!")
q=int(input("Please enter the length of password: "))
a=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
b=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
c=['0','1','2','3','4','5','6','7','8','9']
d=['@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>','*', '(', ')', '<']
e=[]
e=a+b+c+d+e
f=""
for i in range(0,q):
    f=f+r.choice(e)
print("The password generated is: ",f)
print("Thank you for using Password Generator !!")
print("***********")
