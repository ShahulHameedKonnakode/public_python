# quiz project with if else
print("Let's Play a Quiz. Are you ready?! ")

print("***************************")
print("Questions:")
score=0
#question-1
print("1.Who is the father of India ?.")
print("   A. A.P.J. Abdul Kalam \n   B. Mahathma Ghandhi\n   C. Jawaharlal Nehru\n   D. Indira Gandhi\n")
a=input("Enter an option ")
option="b"
if a.lower() == option:
    print("Correct")
    score+=1
else:
    print("Incorrect")
    
#question-2
print("\n2. What is the largest lake in the world?")
print("   A. Caspian Sea \n   B. Baikal \n   C. Lake Superior \n   D. Ontario\n")
a=input ("Enter an option ")
option="b"
if a.lower() == option:
    print("Correct")
    score+=1
else:
    print("Incorrect")

#question-3
print("\n3. Which planet in the solar system is known as the “Red Planet”?")
print("   A. Venus \n   B. Earth \n   C. Mars \n   D. Jupiter\n")
a=input ("Enter an option ")
option="c"
if a.lower() == option:
    print("Correct")
    score+=1
else:
    print("Incorrect")

# question-4
print("\n4. Who wrote the novel “War and Peace”?")

print("   A. Anton Chekhov \n   B. Fyodor Dostoevsky \n   C. Ivan Turgenev \n   D. Leo Tolstoy\n")
a=input ("Enter an option ")
option="d"
if a.lower() == option:
    print("Correct")
    score+=1
else:
    print("Incorrect")


# qestion-5
print("\n5. What is the capital of Japan?")

print("   A. Beijing \n   B. Tokyo \n   C. Seoul \n   D. Bangkok\n")
a=input ("Enter an option ")
option="b"
if a.lower() == option:
    print("Correct")
    score+=1
else:
    print("Incorrect")






# Printing Score
print("\nYour Score is: ",score)

# salutation
if score == 1:
    print("Good!!")
elif score == 2:
    print("Very Good!!")
elif score == 3:
    print("Excellent!!")
elif score == 4:
    print("Awesome!!")
else:
    print("Sorry, Please try again")