import random

player = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
computer = random.randint(0, 2)

if player == 0:
    print("""    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)\n""")
elif player == 1:
    print("""    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)\n""")
elif player == 2:
    print("""    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)\n""")
else:
    print(" ")

print("Computer chose:\n")

if computer == 0:
    print("""    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)\n""")
elif computer == 1:
    print("""    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)\n""")
elif computer == 2:
    print("""    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)\n""")

if player == computer:
    print("It's a draw")
elif (player == 0 and computer == 1) or (player == 1 and computer == 2) or (player == 2 and computer == 0):
    print("You lose")
elif (player == 0 and computer == 2) or (player == 1 and computer == 0) or (player == 2 and computer == 1):
    print("You win!")
else:
    print("Please try again")
    