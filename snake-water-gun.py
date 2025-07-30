import random
import time
from colorama import Fore, init
from datetime import datetime
import os

init(autoreset=True)

# Mapping for choices
youDict = {"s": 1, "w": -1, "g": 0}
reverseDict = {1: "Snake", -1: "Water", 0: "Gun"}

def countdown():
    print(Fore.YELLOW + "Get ready!", end=" ")
    for num in ["3️⃣", "2️⃣", "1️⃣", "🔫"]:
        print(Fore.CYAN + num, end=" ", flush=True)
        time.sleep(0.7)
    print("\n")

def play_game():
    print(Fore.MAGENTA + "🎮 Welcome to the Snake Water Gun Game!")
    name = input("Enter your name: ")

    try:
        rounds = int(input("How many rounds do you want to play? (e.g., 3, 5, 7): "))
    except ValueError:
        print(Fore.RED + "⚠️ Invalid number! Defaulting to 3 rounds.")
        rounds = 3

    your_score = 0
    computer_score = 0
    history = []

    for i in range(1, rounds + 1):
        print(Fore.BLUE + f"\n🔁 Round {i}")
        countdown()

        computer = random.choice([-1, 0, 1])
        youstr = input("Choose S for Snake, W for Water, G for Gun: ").lower()

        if youstr not in youDict:
            print(Fore.RED + "❌ Invalid input! Skipping this round.")
            history.append(f"Round {i}: Invalid input by {name}")
            continue

        you = youDict[youstr]

        print(Fore.LIGHTGREEN_EX + f"{name} chose {reverseDict[you]}")
        print(Fore.LIGHTRED_EX + f"Computer chose {reverseDict[computer]}")

        if you == computer:
            result = "Draw"
            print(Fore.YELLOW + "🤝 It's a draw!")
        elif (computer == -1 and you == 1) or (computer == 1 and you == 0) or (computer == 0 and you == -1):
            result = "You Win"
            print(Fore.GREEN + "✅ You win this round!")
            your_score += 1
        else:
            result = "Computer Wins"
            print(Fore.RED + "❌ Computer wins this round!")
            computer_score += 1

        history.append(f"Round {i}: {name} chose {reverseDict[you]}, Computer chose {reverseDict[computer]} – {result}")

    print(Fore.MAGENTA + "\n📊 Final Scores:")
    print(Fore.LIGHTCYAN_EX + f"{name}: {your_score}")
    print(Fore.LIGHTCYAN_EX + f"Computer: {computer_score}")

    if your_score > computer_score:
        print(Fore.GREEN + "🏆 You won the game!")
    elif your_score < computer_score:
        print(Fore.RED + "😢 You lost the game!")
    else:
        print(Fore.YELLOW + "🤝 It's a tie!")

    print(Fore.LIGHTWHITE_EX + "\n📜 Match Recap:")
    for line in history:
        print(Fore.LIGHTBLUE_EX + line)

    # Save to file inside "Game_logs" folder
    if not os.path.exists("Game_logs"):
        os.makedirs("Game_logs")
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"Game_logs/{name}_match_{timestamp}.txt"

    with open(filename, "w" ,encoding="utf-8") as file:
        file.write(f"🎮 Match Recap for {name} – {timestamp}\n")
        file.write("-" * 40 + "\n")
        for line in history:
            file.write(line + "\n")
        file.write(f"\nFinal Scores:\n{name}: {your_score}\nComputer: {computer_score}\n")
    print(Fore.LIGHTYELLOW_EX + f"\n📁 Match history saved to '{filename}'")

while True:
    play_game()
    again = input(Fore.MAGENTA + "\nDo you want to play again? (y/n): ").lower()
    if again != 'y':
        print(Fore.LIGHTMAGENTA_EX + "Thanks for playing! 💖")
        break
    print(Fore.LIGHTMAGENTA_EX + "Starting a new game...\n")
