import random

options = ["Rock", "Paper", "Scissors"]

user_choice = input("Choose Rock,Paper or Scissors: ")

computer_choice = random.choice(options)

print("You choose: ", user_choice) # no comments
print("Computer choose: ",computer_choice)

if user_choice == computer_choice:
    print("Its a tie")
elif user_choice == "Rock" and computer_choice == "Scissors":
    print("Rock smashes scissors! You win")
elif user_choice == "Paper" and computer_choice == "Rock":
    print("Paper covers Rock! You win")
elif user_choice == "Scissors" and computer_choice == "Paper":
    print("Scissor cuts paper, You win")
else:
    print("Bro you are ass, dogwater. Imagine losing to a ai ")