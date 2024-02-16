import random
while True:
 print("&&&&&&&&&&&&&&&")
 print("Welcome to Rock,Paper and Scissor game !!")
 print("Please choose any ane of the options: ")
 print("1. Rock")
 print("2. Paper")
 print("3. Scissors")
 a=int(input("Your choice: "))
 if (a==1):
    print("You chose: Rock")
 elif (a==2):
    print("You chose: Paper")
 elif (a==3):
    print("You chose: Scissors")
 else:
    print("Invalid Input")
 b=["Rock","Paper","Scissors"]
 c=random.choice(b)
 print("The computer chose: ",c)
 if(a==1 and c=="Paper"):
    print("The Computer won the game!")
 elif(a==1 and c=="Scissors"):
    print("Congratulations! You won the game!")
 elif (a==1 and c=="Rock"):
    print("It's a tie!")
 elif (a==2 and c=="Rock"):
    print("Congratulations! You won the game!")
 elif (a==2 and c=="Scissors"):
    print("The Computer won the game!")
 elif (a==2 and c=="Paper"):
    print("It's a tie!")
 elif (a==3 and c=="Rock"):
    print("The Computer won the game!")
 elif (a==3 and c=="Scissors"):
    print("It's a tie!")
 h=input("Do you want to continue to play the game ? : ")
 if (h=="NO" or h=="no"):
      print("Thank you for playing the game !!")
      break
 elif (h=="YES" or h=="yes"):
      continue
