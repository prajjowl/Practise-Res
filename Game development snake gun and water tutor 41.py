#_58_Soham_ Nalawade
#1 year ago
#written in easily understandable code
#**After each round result get displayed with proof **
"""
import random
import time
print("*** GAME BEGIN *****")
time.sleep(2)
print("Let's start the snake,water an gun game")
print("NOTE:: you have only 10 chance")
i=0
d=0
computer=0
user=0
while(i<10):
    lst=["snake","water","gun"]
    ch=random.choice(lst)
    x=input("Enter 's' for snake,Enter'w' for water,Enter 'g' for gun::")

    if ch=='snake' and x=='s':
        print("computer selected:", ch)
        print("draw")
        d=d+1
        i=i+1
    elif ch=='snake' and x=='w':
        print("computer selected:", ch)
        print("computer win this game")
        computer=computer+1
        i = i + 1
    elif ch == 'snake' and x == 'g':
        print("computer selected:", ch)
        print("you win this game")
        user=user + 1
        i = i + 1
    elif ch == 'water' and x == 's':
        print("computer selected:", ch)
        print("you win this game")
        user=user+ 1
        i = i + 1
    elif ch == 'water' and x == 'g':
        print("computer selected:", ch)
        print("coputer win this game")
        computer=computer + 1
        i = i + 1
    elif ch=='water' and x=='w':
        print("computer selected:", ch)
        print("draw")
        d=d+1
        i = i + 1
    elif ch == 'gun' and x == 'w':
        print("computer selected:", ch)
        print("you win this game")
        user=user+ 1
        i = i + 1
    elif ch == 'gun' and x == 's':
        print("computer selected:", ch)
        print("computer win this game")
        computer=computer + 1
        i = i + 1
    elif ch == 'gun' and x == 'g':
        print("computer selected:", ch)
        print("draw")
        d = d + 1
        i = i + 1
        """
"""
print("Draw matches are:",d)
print("you won matches are:",user)
print("computer won matches are:",computer)
if user>computer:
    print("Congrates!! you are WINNER of this game ")
    time.sleep(2)
    print("!!Winner Winner Chiken Dinner!!")
elif computer>user:
    print ("computer won this game!!")
    time.sleep(2)
    print("**Try again**")
elif computer==user:
  #  print("Match draw")
   """
import random
print("****GameBEGIN****")
print("Lets start the game ")
print("You have only 10 chance ")
i=0
d=0
computer=0
user=0
while(i<=10):
    lst=["Snake","Water","Gun"]
    ch=random.choice(lst)
    x=input("Enter s for snake,w for water,g for gun::")
    if ch=='Snake'and x=="s":
        print("Computer selected",ch)
        print("It is draw ")
        d=d+1
        i=i+1
    elif ch=='Snake'and x=="w":
        print("Computer selected ",ch)
        print("computer is  winner ")
        computer=computer+1
        i=i+1
    elif ch=='Snake'and x=="g":
        print("Computer selected",ch)
        print("you are winner ")
        user=user+1
        i=i+1
    elif ch=='Water'and x=='s' :
        print("Computer selected",ch)
        print("You are winner  ")
        computer=computer+1
        i=i+1
    elif ch=='Water'and x=='w' :
        print("Computer Selected",ch)
        print("Draw")
        d=d+1
        i=i+1
    elif ch=='Water' and x=='g':
        print("Computer selected",ch)
        print("COmputer is winner ")
        computer=computer+1
        i=i+1
    elif ch=='Gun'and x=='s':
        print("Computer is selected",ch)
        print("Computer is winner")
        computer+1
        i=i+1
    elif ch=='Gun' and x=='w':
        print("Computer is selected",ch)
        print("You are winner")
        user=user+1
        i=i+1
    elif ch=='Gun' and x=='g':
        print("Computer is selected",ch)
        print("Draw")
        d=d+1
        i=i+1
    else:
        print("It is invalid ")
print("Draw matches are",d)
print("Computer wins are",computer)
print("You are winner",user)
if user>computer:
    print("you are winner of the game ")
    print("Winner Winner Chicken Dinner ")
elif computer>user:
    print("Computer are winner " )
elif computer==user:
    print("Draw")






