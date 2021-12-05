print('''

888                                                          
888                                                          
888                                                          
888888888d888 .d88b.  8888b. .d8888b 888  888888d888 .d88b.  
888   888P"  d8P  Y8b    "88b88K     888  888888P"  d8P  Y8b 
888   888    88888888.d888888"Y8888b.888  888888    88888888 
Y88b. 888    Y8b.    888  888     X88Y88b 888888    Y8b.     
 "Y888888     "Y8888 "Y888888 88888P' "Y88888888     "Y8888 
 
 d8b        888                     888 
Y8P        888                     888 
           888                     888 
888.d8888b 888 8888b. 88888b.  .d88888 
88888K     888    "88b888 "88bd88" 888 
888"Y8888b.888.d888888888  888888  888 
888     X88888888  888888  888Y88b 888 
888 88888P'888"Y888888888  888 "Y88888 
 
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
choice_1 = input("You're at a crossroad, where do you want to go?\n"
                 "Type \"l\" (for left) or \"r\" (for right). ").lower()

if choice_1 == 'r':
    print("Aaaagggghhhhhhhhh!!!! You've walked right off a cliff!")
    print("Game Over.")
elif choice_1 == 'l':
    choice_2 = input("Great choice!\n"
                     "You've now reached a lake that you'll need to cross in order to get to the treasure.\n"
                     "Would you like to swim across or build a raft?\n"
                     "Type \"s\" (for swim) or \"b\" (for build a raft). ").lower()
    if choice_2 == 's':
        print("Gulp! You've been attacked by piranha!")
        print("Game Over.")
    elif choice_2 == 'b':
        choice_3 = input("Right again! You have now arrived at a set of doors\n"
                         "Each door is one of the colors of the rainbow.\n"
                         "Just type the right color to get to the treasure!\n"
                         "If you pick the wrong color, you die!\n"
                         "No pressure! Good luck!!! ").lower()
        if choice_3 == 'indigo':
            print("Congratulations!!! You found the treasure!!!")
            print('''
            *******************************************************************************
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
            /______/______/______/______/______/______/______/______/______/______/_______/
            *******************************************************************************
            ''')
        elif choice_3 == 'red':
            print("Yikes!!! You just walked into a pool of lava!!!")
            print("Game Over.")
        elif choice_3 == 'blue':
            print("Oh no!!! You've been eaten by the Creature From The Black Lagoon!!!")
            print("Game Over.")
        else:
            print("Trap door! You've fallen to your death!!!")
            print("Game Over.")
    else:
        print("That's an invalid answer which is an automatic death.")
        print("Game Over.")

else:
    print("That's an invalid answer which is an automatic death.")
    print("Game Over.")
