from colorama import Fore, Back
import random

count = 0
final_result = 0
games_played = 1
new_game = True
difficulty = ""
computer_number = random.randint(1, 100)
print("The computer picked a number!")

while True:
    if new_game:
        difficulty = input("Choose a difficulty: [e]asy(10 Attempts), [n]ormal(5 Attempts), [h]ard(3 Attempts), [i]mpossible(1 Attempt): ")
        if difficulty == "e":
            difficulty = 10
            new_game = False
        elif difficulty == "n":
            difficulty = 5
            new_game = False
        elif difficulty == "h":
            difficulty = 3
            new_game = False
        elif difficulty == "i":
            difficulty = 1
            new_game = False
        else:
            print(Fore.RED + "Invalid difficulty. Try again...")
            print(Fore.RESET + "")
            continue
        print(Fore.RESET + "")
    if count == difficulty:
        print(Fore.RED + "You lose! No more attempts left.")
        print(Fore.RESET + "")
        decision = input("Type [y] to Play Again or [n] to quit: ")
        if decision == "y":
            new_game = True
            computer_number = random.randint(1, 100)
            games_played += 1
            count = 0
            continue
        elif decision == "n":
            print(Back.WHITE + Fore.BLACK + "Thank you for playing!")
            print(f"You won {final_result}/{games_played} games!")
            break
    current_guess = int(input("Guess the number (1-100): "))
    count += 1
    if current_guess > computer_number:
        print(Fore.GREEN + "Too High!")
        print(Fore.YELLOW + f"{difficulty - count} attempts remaining.")
        print(Fore.RESET + "")
    elif current_guess < computer_number:
        print(Fore.RED + "Too Low!")
        print(Fore.YELLOW + f"{difficulty - count} attempts remaining.")
        print(Fore.RESET + "")
    elif current_guess == computer_number:
        final_result += 1
        print(Fore.BLUE + f"Congratulations! You Guess it in {count} attempts!")
        print(Fore.RESET + "")
        decision = input("Type [y] to Play Again or [n] to quit: ")
        if decision == "y":
            new_game = True
            computer_number = random.randint(1, 100)
            games_played += 1
            count = 0
            continue
        elif decision == "n":
            print(Back.WHITE + Fore.BLACK + "Thank you for playing!")
            print(f"You won {final_result}/{games_played} games!")
            break




