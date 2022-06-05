import random

user_choice = input("Welcome to Rock Paper Scissors game. Enter R for Rock, P for Paper or S for Scissors: ").lower()
while user_choice != "rock" and user_choice != "paper" and user_choice != "scissors":
    user_choice = input("Invalid input, please try again: ").lower()

possible_choice = ["rock", "paper", "scissors"]
cpu_choice = random.choice(possible_choice)
# random_num = random.randint(0,2)

# if random_num == 0:
#     cpu_choice = "rock"
# elif random_num == 1:
#     cpu_choice = "paper"
# elif random_num == 2:
#     cpu_choice = "scissors"

print()
print("Your Choice:", user_choice)
print("Computer's Choice:", cpu_choice)

if user_choice == "rock":
    if cpu_choice == "rock":
        print("It's a tie!")
    elif cpu_choice == "paper":
        print("You lost!")
    elif cpu_choice == "scissors":
        print("You win!")
elif user_choice == "paper":
    if cpu_choice == "paper":
        print("It's a tie!")
    elif cpu_choice == "scissors":
        print("You lost!")
    elif cpu_choice == "rock":
        print("You win!")
elif user_choice == "scissors":
    if cpu_choice == "scissors":
        print("It's a tie!")
    elif cpu_choice == "rock":
        print("You lost!")
    elif cpu_choice == "paper":
        print("You win!")
