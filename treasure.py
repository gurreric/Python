print("Welcome to Treasure Isle.")
firststep =input("Do you wish to go left or right?").lower()
if firststep =="left":
    print("You're on the right track!")
    swim =input("Do you want to swim or wait?").lower()
    if swim =="swim":
        print("Welp, you dead.")
    else:
        print("Good idea. Boat is here.")
        door = input("Chose door, Blue, Red, or Yellow").lower()
        if door =="red":
            print("Fire! Game Over")
        elif door =="Blue":
            print("Monster go ya, game over.")
        elif door=="yellow":
            print("Found the treasure.")

else:
    print("You fell into a hold.") 


