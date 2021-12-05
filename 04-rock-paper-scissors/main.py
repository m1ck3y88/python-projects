import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game_images = [rock, paper, scissors]

while True:
    try:
        user_choice = int(
            input("Welcome to Rock, Paper, Scissors! Type \"0\" to choose rock, \"1\""
                  " to choose paper, or \"2\" to choose scissors. "))
        if user_choice >= 3 or user_choice < 0:
            print("You typed an invalid number, you lose!")
        else:
            print(game_images[user_choice])
            if user_choice == 0:
                print("You chose Rock!\n")
            elif user_choice == 1:
                print("You chose Paper!\n")
            else:
                print("You chose Scissors!\n")
    except:
        print("Invalid entry. Please try again.")
        continue
    else:
        break

computer_choice = random.randint(0, 2)
if computer_choice == 0:
    print("\nComputer chose Rock!")
elif computer_choice == 1:
    print("\nComputer chose Paper!")
else:
    print("\nComputer chose Scissors!")
print(game_images[computer_choice])

if user_choice == 0 and computer_choice == 2:
    print("You win!")
elif computer_choice == 0 and user_choice == 2:
    print("You lose.")
elif computer_choice > user_choice:
    print("You lose.")
elif user_choice > computer_choice:
    print("You win!")
elif user_choice == computer_choice:
    print("It's a draw!")
