'''
QUIZ MASTER PROJECT
-------------------
The criteria for the project are on the website. Make sure you test this quiz with 
two of your student colleagues before you run it by your instructor.
'''
score = 0
print("Question: 1 \n \rA bus fell over, 5 kids left from the roof and 4 left from the door")
answer1 = input("How many kids left the bus? \n") #Question 1
if answer1 == ("9") or answer1.lower() == ("9 kids"):
    score += 1
    print("You are correct! \n \rThe kids are ok by the way!")
else:
    print("The answer is not",answer1,"the correct answer is 9")

print("\n\n\rQuestion: 2 \n\rWhat's the name of Spongebobs pet?") #Question 2
answer2 = input()
if answer2.lower() == ("gary"):
    score += 1
    print("You are correct!")
else:
    print("His pet isn't",answer2,"It's actually Gary")
print("\n\n\rQuestion: 3 \n\rHow do you ask a question in python?") #Question 3
answer3 = input("A: ask.input() \n\rB: ask() \n\rC: input()\n\r")
if answer3.lower() == ("c"):
    score += 1
    print("You are correct!")
else:
    print("The correct answer isn't",answer3,"it's C")
print("\n\n\rQuestion: 4 \n\rWho shot first Han Solo or Greedo?") #Question 4
answer4 = input("")
if answer4.lower() == ("han solo") or answer4.lower() == ("han"):
    score += 1
    print("You are definitely an intellectual")
else:
    print("HAN SHOT FIRST YOU NERF HERDER")
print("\n\n\rQuestion: 5 \n\rDogs or Cats?") #Question 5
answer5 = input("")
if answer5.lower() == ("dogs"):
    score += 1
    print("You are the better part of humanity")
else:
    print("The answer is obviously dogs \n\rYou should get help")
if score > 4:
    print("You did great!")
elif score <=4:
    print("You could have done better :(")