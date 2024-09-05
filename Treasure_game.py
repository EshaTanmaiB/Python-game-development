print('''*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
choice1 = input("Your at a crossboard, where do you want to go? left or right?")
if choice1 == "left":
    choice2 = input('Your at a beach, you can either swim or wait.'
                     'There is an Island at the middle of a beach.\n'
                     'Type "swim" to swim across.\n'
                     'Type "wait" to wait for a boat.'
                     ).lower()
    if choice2 == "wait":
        choice3 = input('You arrive to the Island unharmed.'
              'There are three doors through which you can go into.\n'
              'Pick a door, "Red", "Yellow", "Blue"')
        if choice3 == "Red":
            print("It's a room full of fire. Game over ! ")
        elif choice3 == "Yellow":
            print("You found the treasure. You win !")
        elif choice3 == "Blue":
            print("It's a room full of crocodiles. Game over !")

    else:
        print("Game over !")
else:
    print("Game over !")
