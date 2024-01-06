# Roller Coaster
print("Welcome to the roller coaster app!")
#declare variables
height = int(input("What is you heigh in cm?"))
age = int(input("What is your age?"))
price =float()
# Check for height:
# Build nested if statement
if height >= 120:
    print("you're tall enough")
    if age <= 18:
        print("Your ticket is $7")

    else:
        price = 12
        print(f"Your ticket costs {price}")



else:
    print("sorry, moose out front should have told ya.")
