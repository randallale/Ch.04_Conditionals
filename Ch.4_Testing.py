'''
a = True
if a:
    print("a is true!")
else:
    print("a is false!")

temperature = int(input("What is the temperature in Fahrenheit? "))
if temperature > 90:
    print("It is hot outside")
else:
    print("It is not hot outside")
print("Done")

#FIX THIS CODE
temperature = int(input("What is the temperature in Fahrenheit? "))
if temperature > 90:
    if temperature > 110:
        print("Oh man, you could fry eggs on the pavement!")
    else:
        print("It is hot outside")
elif temperature < 30:
    print("It is cold outside")
else:
    print("It is ok outside")
print("Done")
#FIX THIS CODE^^^ I set it to if the temp is greater than 90 it will also ask if the temp is above 110 and if it is it will say the correct statement
'''
jedi = input("Who is the greatest Jedi Master? ")
if jedi.lower() == "yoda":
    print("Greatest, he is!")
else:
    print("Incorrect")