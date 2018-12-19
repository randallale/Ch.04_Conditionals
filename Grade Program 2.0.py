print("What's your current semester grade?")
current = int(input())
print("What was the final exam grade?")
final_grade = int(input())
print("What was the final's weight")
weight = int(input())

overall = (100-weight)*current+(weight*final_grade)
overall = overall/100
print("You got a ", end= str(overall))
print('%')
if overall < 59:
    print("You got an F! \n \rYou should go to johnston!")
elif overall >= 60 and overall <= 69:
    print("You got a D! \n \rWhy are you going to urbandale??")
elif overall >= 70 and overall <= 79:
    print("You got a C! \n \rTry harder next year!")
elif overall >= 80 and overall <= 89:
    print("You got a B! \n \rYou did pretty good!")
elif overall >= 90 and overall <= 100:
    print("You got an A! \n \rYOU WERE AMAZING!")