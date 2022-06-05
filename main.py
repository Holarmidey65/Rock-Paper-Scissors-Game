import random

print("Welcome to Rock Paper Scissors game. Enter - \n R for Rock \n P for Paper \n S for Scissors")

choice = str(input("Enter [R], [P] or [S]: ")).lower()
while choice != "r" and choice != "p" and choice != "s":
    choice = input("Invalid input, please try again: ").lower()

possible_choice = ["Rock", "Paper", "Scissors"]
cpu_choice = random.choice(possible_choice)

if choice == "r":
    user_choice = "Rock"
elif choice == "p":
    user_choice = "Paper"
else:
    user_choice = "Scissors"

print()
print("Your Choice:", user_choice)
print("Computer's Choice:", cpu_choice)

if user_choice == "Rock":
    if cpu_choice == "Rock":
        print("It's a tie!")
    elif cpu_choice == "Paper":
        print("You lost!")
    elif cpu_choice == "Scissors":
        print("You win!")
elif user_choice == "Paper":
    if cpu_choice == "Paper":
        print("It's a tie!")
    elif cpu_choice == "Scissors":
        print("You lost!")
    elif cpu_choice == "Rock":
        print("You win!")
elif user_choice == "Scissors":
    if cpu_choice == "Scissors":
        print("It's a tie!")
    elif cpu_choice == "Rock":
        print("You lost!")
    elif cpu_choice == "Paper":
        print("You win!")
