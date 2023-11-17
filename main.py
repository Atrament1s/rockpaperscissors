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

user_choice = int(input("Type 0 for rock, 1 for paper, or 2 for scissors\n"))

if user_choice >= 3 or user_choice < 0:
    print("Invalid number, please input 0, 1, or 2 for rock, paper, or scissors, respectively.")
else:
    print("You Chose:")
    print(game_images[user_choice])

    computer_choice = random.randint(0, 2)
    print("Computer Chose:")
    print(game_images[computer_choice])
    if user_choice == 0 and computer_choice == 2:
        print('You win!')
    elif computer_choice == 0 and user_choice == 2:
        print("You lose!")
    elif computer_choice > user_choice:
        print("You lose!")
    elif computer_choice < user_choice:
        print("You win!")
    elif computer_choice == user_choice:
        print("It's a tie!")
