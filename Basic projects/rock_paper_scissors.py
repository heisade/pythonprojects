import random


def bot_choice():
    bot = ['rock', 'paper', 'scissors']
    bot_random = random.choice(bot)
    return bot_random

#bot_choice = rps()
print(bot_choice())

print("================== Welcome to Rock, Paper, Scissors ==================")

while True:
    user_choice = input("Enter Rock or Paper or Scissors: ").lower()
    choice = ["rock", "paper", "scissors"]
    if user_choice not in choice:
        print("Invalid Input!")
    else:
        # Get the bot's choice
        bot_selection = bot_choice()
        
        # For wins
        if user_choice == 'rock' and bot_selection == 'scissors':
            print("You win!!")
        elif user_choice == 'paper' and bot_selection == 'rock':
            print("You win!!")
        elif user_choice == 'scissors' and bot_selection == 'paper':
            print("You win!!")
        # For draws
        elif user_choice == 'rock' and bot_selection == 'rock':
            print("It's a draw!")
        elif user_choice == 'paper' and bot_selection == 'paper':
            print("It's a draw!")
        elif user_choice == 'scissors' and bot_selection == 'scissors':
            print("It's a draw!")
        # For loses
        else:
            print("You lose")
            print(f"Bot chose {bot_selection}")