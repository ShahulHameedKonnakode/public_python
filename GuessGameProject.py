import string
import random


#Guess Number Game Project
'''
Project Desciption:
This project is desined for...


'''
# function

# fuction for level-1
def guessGame_Level_1():
    random_number=random.randrange(1,10) 
    for i in range(1,4):
        gussed_number=int(input("Guess A Number: "))
        
        if gussed_number==random_number:
            print("Excellent")
            break
        else:
            print("Sorry! Try Again")
            print("You have left",3-i, "Chance")
    else:
        print("Game is Over")
        print("System Guessed Number is",random_number)
        print("The number you guessed is", gussed_number)

    
# fuction for level-2
def guessGame_Level_2():
    random_letters=random.choice(string.ascii_letters)
    for i in range(1,4):
        gussed_letter=input("Guess A Letter: ")
        
        if gussed_letter==random_letters:
            print("Excellent")
            break
        else:
            print("Sorry! Try Again")
            print("You have left",3-i, "Chance")
    else:
        print("Game is Over")
        print("System Guessed Letter is",random_letters)
        print("The Letter You Guessed is", gussed_letter)


# fuction for level-3
def guessGame_Level_3():
    random_number=random.randrange(1,100) 
    for i in range(1,4):
        gussed_number=int(input("Guess A Number: "))
        
        if gussed_number==random_number:
            print("Excellent")
            break
        else:
            print("Sorry! Try Again")
            print("You have left",3-i, "Chance")
    else:
        print("Game is Over")
        print("System Guessed Number is",random_number)
        print("The number you guessed is", gussed_number)

# Game Rules:
def gameRulesLevel_1():
    print("📢📢GAMES RULES📢📢")
    print("************")
    print('''1. Guess a number between(1-10) and input it\n2. The player has a limited number of attempts (You have 3 Chances to try).
3. After the allowed attempts, reveal the correct number and end the game.
💥💥 Let's Start 💥💥\n ****************\n''')

def gameRulesLevel_2():
    print("📢📢GAMES RULES📢📢")
    print("************")
    print('''1. Guess a letter(A-Z/a-z) and input it\n2. The player has a limited number of attempts (You have 3 Chances to try).
3. After the allowed attempts, reveal the correct letter and end the game.
💥💥 Let's Start 💥💥\n ****************\n''')

def gameRulesLevel_3():
    print("📢📢GAMES RULES📢📢")
    print("************")
    print('''1. Guess a number between(1-100) and input it\n2. The player has a limited number of attempts (You have 3 Chances to try).
3. After the allowed attempts, reveal the correct number and end the game.
💥💥 Let's Start 💥💥\n ****************\n''')
    

# main

print("🎉🎉 WELCOME TO GUESS GAME 🎉🎉")
print("***********************")

player_name=input("Enter Your Name Please:  ")

print("Hi",player_name,"You are Welcome to World of Game!!!🚀🚀 ")
choice=input("Are You Ready to Play? (Y/N):   ").lower()
print()
if choice=="y":
    level=int(input('''✅ Please Select a Level✅\n*********************\n1. Level-1\n2. Level-2\n3. Level-3\nEnter Your Level:  '''))
    
    if level==1:
        gameRulesLevel_1()
        guessGame_Level_1()
    elif level==2:
        gameRulesLevel_2()
        guessGame_Level_2()
    elif level==3:
        gameRulesLevel_3()
        guessGame_Level_3()
elif choice=="n":
    print("Ok, Thank you, Try next time")
else:
    print('invalid option')


    
    


  






