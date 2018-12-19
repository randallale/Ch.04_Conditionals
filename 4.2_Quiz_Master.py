'''
QUIZ MASTER PROJECT
-------------------
The criteria for the project are on the website. Make sure you test this quiz with 
two of your student colleagues before you run it by your instructor.
'''
score = 0
print("Question 1 \n \rA bus fell over, 5 kids left from the roof and 4 left from the door")
answer1 = input("How many kids fell off the bus \n")
if answer1 == ("9") or answer1.lower() == ("9 kids"):
    score += 1
    print("You are correct! \n \rThe kids are ok by the way!")
else:
    print("The answer is not",answer1,"the correct answer is 9")