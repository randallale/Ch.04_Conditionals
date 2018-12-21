'''
HONOR CODE: I solemnly promise that while taking this test I will only use PyCharm or the Internet,
but I will definitely not ask another person except the instructor. Signed: ______________________


  1. What is missing from this code?
     
     midichlorians = float(input("Enter midichlorian count: ")
     if midichlorians > 10000:
         print("You have serious Jedi potential")
     else:
         print("Jedi, you will never be.")
'''
     #the first line of code is missing a ) at the end of the line
     
     
'''
  2. This runs, but there is something wrong. What is it?
     
     user_input = input("R2D2 is a: ")
     print("A. Droid")
     print("B. Storm Trooper")
     if user_input.upper() == "A":
         print("Correct!")
     else:
         print("Incorrect.")
'''



'''
     
  3. There are two things wrong with this code that tests if x is set to a
     positive value. One prevents it from running, and the other is subtle.
     Make sure the if statement works no matter what x is set to.
     Identify both issues. 
     
     x == 4
     if x >= 0:
         print("x is positive.")
     else:
         print("x is not positive.")
 '''
 # x==4 would need to change to x=4
 
 
 '''
  4. What three things are wrong with the following code?
     
     x = input("Enter a number: ")
     if x = 3
         print("You entered 3")
 '''
 #1: Before input you need a float/int
 #2: : should be after the 3 in the second line
 #3: the = should be ==
 
 '''
  5. There are four things wrong with this code. Identify all four issues. 
     
     answer = input("What is the name of Poe Dameron's Droid? ")
     if a = "BB8":
         print("Correct!")
         else
         print("Incorrect! It is BB8.")
'''
#1: if a = "BB8": should be a == "BB8":
#2: if a = "BB8": should be a == ("BB8"):
#3: else should be like else:
#4: else should not be indented

'''
  6. This program doesn't work correctly. What is wrong?
     
     x = input("Who are the top 3 greatest Jedi?")
     if x == "Yoda" or "Luke Skywalker" or "Obi-Wan Kenobi":
         print("That is correct!")
'''
# you need to ask x == after every or not just in the beginning


'''
  7. Look at the code below. Write your best guess here on what it will print.
     Next, run the code and see if you are correct.
     Clearly label your guess and the actual answer.
     
     x = 5
     y = x == 6
     z = x == 5
     print("x=", x)
     print("y=", y)
     print("z=", z)
     if y:
         print("Star Wars Episodes 1,2,3 are the best!")
     if z:
         print("Star Wars Episodes 4,5,6 are the best!")
'''
#Guess: It makes all of the variables equal to 5 and then makes y true if equal to 6 and x true if equal to 5
#Guess: It then will print out the if z: statement because it is true
# My guess was right ;) the answer was the if z: statement

'''
 8. Look at the code below. Write you best guess on what it will print.
     Next, run the code and see if you are correct. 
     
     x = 5
     y = 10
     z = 10
     print(x < y)
     print(y < z)
     print(x == 5)
     print(not x == 5)
     print(x != 5)
     print(not x != 5)
     print(x == "5")
     print(5 == x + 0.00000000001)
     print(x == 5 and y == 10)
     print(x == 5 and y == 5)
     print(x == 5 or y == 5)
'''
# I will guess and what each one will print
# 1: True
# 2: False
# 3: True
# 4: False
# 5: False
# 6: True
# 7: False
# 8: False
# 9: True
# 10: False
# 11: True
# I got them all right

'''''
 9. Look at the code below. Write you best guess on what it will print.
     Next, run the code and see if you are correct. (HINT: when comparing strings, ASCII codes are used. https://www.ascii-code.com/)
'''''
     print("3" == "3")
     print(" 3" == "3")
     print(3 < 4)
     print("3" < "4")
     print("3" < 4)
     print("<" < ">")
     print((2 == 2) == "True")
     print((2 == 2) == True)
     print("?"<"!")

#1: True
#2: False
#3: True
#4: False -- Got wrong
#5: False --- Doesn't even run
#6: True
#7: False
#8: True
#8: False
# I tried to run it but it couldn't run

'''
 10. What things are wrong with this section of code?
     The programmer wants to set the force sensitivity variable according to the character the user selects.
     
     print("Welcome to the Jedi Academy!")

     print("A. Jedi Master")
     print("B. Sith Lord")
     print("C. Droid")

     user_input = input("Choose a character?")

     if user_input = A:
         money = 1000
     else if user_input = B:
         money = 900
     else if user_input = C:
         money = 0
'''
# I would make the code this \/\/\/\/\/
print("Welcome to the Jedi Academy!")

print("A. Jedi Master")
print("B. Sith Lord")
print("C. Droid")

user_input = input("Choose a character?")

if user_input.upper() == ("A"):
    money = 1000
elif user_input.upper() == ("B"):
    money = 900
elif user_input.upper() == ("C"):
    money = 0
