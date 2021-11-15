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

#Write your code below this line 👇

import random

game_images = [rock, paper, scissors]

user_choice = int(input("What do you chose? Type 1 for Rock, 2, for Paper, or 3 for Scissors.\n"))

if user_choice >= 4 or user_choice < 1:
  print("You entered an invalid number.\n")
  user_choice = int(input("Please type: 1 for Rock, 2, for Paper, or 3 for Scissors.\n"))

computer_choice = random.randint(1,3)

print("You chose: \n" + game_images[user_choice -1] + "\n")
print("The computer chose: \n" + game_images[computer_choice -1] + "\n")

if user_choice == 1 and computer_choice == 3:
  print("You win.")
elif user_choice == 3 and computer_choice == 1:
  print("You lose.")
elif int(user_choice) == int(computer_choice):
  print("It is a draw.")
elif int(user_choice) > int(computer_choice):
  print("You win.")  
else:
  print("You lose.")  
