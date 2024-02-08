print("CALCULATOR")
while True:
 print("*********")
 a=int(input("Enter first number: "))
 b=int(input("Enter second number: "))
 print("*********")
 print("Please select an operation: ")
 print("1. Addition")
 print("2. Subtraction")
 print("3. Multiplication")
 print("4. Division")
 print("*********")
 c=int(input("Enter the operation serial no. : "))
 if c in (1,2,3,4,5):
  if (c==1):
    d=a+b
    print("The addition of the input is: ",d)
  elif (c==2):
    e=a-b
    print("The subtraction of the input is: ",e)
  elif (c==3):
    f=a*b
    print("The multiplication of the input is: ",f)
  elif (c==4):
    g=a/b
    print("The division of the input is: ",g)
  print("*********")
  h=input("Do you want to continue to use the calculator ? : ")
  if (h=="NO" or h=="no"):
      break
  elif (h=="YES" or h=="yes"):
      continue
  else:
      print("Invalid input")
      break
 else:
      print("Invalid input")
      break
print("*********")
print("Thank you for using the CALCULATOR !!")