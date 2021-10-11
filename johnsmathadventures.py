import random
from termcolor import colored
from os import sys, system
import time
system("cls")
def add_random():
    a = random.randint(1,10)
    b = random.randint(1,10)
    c = a + b
    print(a," + ",b ," = ?")
    ans = int(input())
    if ans == c:
        print(colored("Your answer Is Correct!","green"))
        return(True)
    else:
        print(colored("The answer is Incorrect!",'red'))
        return(False)
def sub_random(): 
    a = random.randint(1,10)
    b = random.randint(1,10)
    c = a - b
    print(a," - ",b ," = ?")
    ans = int(input())
    if ans == c:
        print(colored("Your answer Is Correct!","green"))
        return(True)
    else:
        print(colored("The answer is Incorrect!",'red'))
        return(False)
def mul_random(): 
    a = random.randint(1,10)
    b = random.randint(1,10)
    c = a * b
    print(a," x ",b ," = ?")
    ans = int(input())
    if ans == c:
        print(colored("Your answer Is Correct!","green"))
        return(True)
    else:
        print(colored("The answer is Incorrect!",'red'))
        return(False)
def div_random():
    while True: 
        a = random.randint(1,10)
        b = random.randint(1,10)
        if a > b:
            break
    c = a / b
    print(a," / ",b ," = ?")
    ans = float(input())
    if ans == c:
        print(colored("Your answer Is Correct!","green"))
        return(True)
    else:
        print(colored("The answer is Incorrect!",'red'))
        return(False)
def intro():
    print(colored("It was a Rainy Humid Evening,","blue"))
    time.sleep(1)
  
   
    print( "John open his Maths Book to solve his math problems he had to complete the HOMEWORK which was given to him buy his math teacher.")
    time.sleep(3)
    print( "The humid weather fromed by the rain made John very sleepy and within some seconds John slept lying down on his table.")
    time.sleep(3)
    input("Press Enter to Continue....")
    system("cls")
    for i in range(101):
        print(colored(f"Loading Math World {i}/100","yellow"))
        time.sleep(0.05)
        system("cls")
    print("John wakes up in the maths world which is full of NUMBERS and SYMBOLS")
    time.sleep(3)
    print(colored("JOHN :","green"),end=" ")
    print("Where Am I ?")
    time.sleep(1)
    print("Then John see a wizard approching which looks like the one on his text book.")
    time.sleep(3)
    print(colored("WIZARD:","yellow"),end=" ")
    print("Hello There!")
    time.sleep(2)
    print(colored("JOHN :","green"),end=" ")
    print("Where am I?")
    time.sleep(1)
    print(colored("WIZARD:","yellow"),end=" ")
    print("Your are Inside the Math World and you need to open the FOUR gates to go to your world!")
    time.sleep(3)
    print(colored("Help John to go to his world....."))
    time.sleep(3)
    input(colored("Press to Continue....","blue"))
    system("cls")

def game():
    print(colored("Welcome To John's Adventures!!!","yellow"))
    print("You have 3 Chances to Clear the FOUR LEVELS")
    print(colored("Press Enter to Start the Game....","blue"))
    lives = 3
    system("cls")
    #LEVEL ONE 
    print(colored("Level 1 Addition","yellow"))
    for i in range(5):
        if add_random():
            pass
        else:
            lives -= 1
            print("Lives Remaining: ",lives)
            if lives==0:
                system("cls")
                print(colored("<<<<GAME OVER>>>>","red"))
                quit()
    print(colored("Level 1 Completed!!!","blue"))
    print(colored("1 st Door is Opened ","blue"))
    input(colored("PRESS ENTER TO CONTINUE","yellow"))
    system("cls")
    #LEVEL 2
    print(colored("Level 2 Subraction","yellow"))
    for i in range(5):
        if sub_random():
            pass
        else:
            lives -= 1
            print("Lives Remaining: ",lives)
            if lives==0:
                system("cls")
                print(colored("<<<<GAME OVER>>>>","red"))
                quit()
    print(colored("Level 2 Completed!!!","blue"))
    print(colored("2 st Door is Opened ","blue"))
    input(colored("PRESS ENTER TO CONTINUE","yellow"))
    system("cls")
    #LEVEL 3
    print(colored("Level 3 Multiplication","yellow"))
    for i in range(5):
        if mul_random():
            pass
        else:
            lives -= 1
            print("Lives Remaining: ",lives)
            if lives==0:
                system("cls")
                print(colored("<<<<GAME OVER>>>>","red"))
                quit()
    print(colored("Level 3 Completed!!!","blue"))
    print(colored("3 st Door is Opened ","blue"))
    input(colored("PRESS ENTER TO CONTINUE","yellow"))
    system("cls")
    #LEVEL 4
    print(colored("Level 4 Addition","yellow"))
    for i in range(5):
        if div_random():
            pass
        else:
            lives -= 1
            print("Lives Remaining: ",lives)
            if lives==0:
                system("cls")
                print(colored("<<<<GAME OVER>>>>","red"))
                quit()
    print(colored("Level 4 Completed!!!","blue"))
    print(colored("4 st Door is Opened ","blue"))
    input(colored("PRESS ENTER TO CONTINUE","yellow"))
    system("cls")
    print(colored("You Have completed the Game!!",'yellow'))
    time.sleep(0.5)
    input("PRESS ENTER TO CONTINUE")
    system("cls")
    print("John wakes up by hearing his mother calling him for dinner. ")
    time.sleep(1)
    print("Then John see his maths book and all his sums have been solved!")
    time.sleep(1)
    print(colored("Thanks For Playing!!",'red'))

intro()
game()
    