import random

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

difficulty_level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
comp_number = random.randint(1, 100)

def game(attempts):
    while attempts > 0:
        print(f"You have {attempts} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))

        if guess == comp_number:
            print(f"You got it! The answer was {comp_number}.")
            return
        elif guess > comp_number:
            print("Too high.\nGuess again.")
        else:
            print("Too low.\nGuess again.")

        attempts -= 1

    print(f"Better luck next time! The number was {comp_number}.")

attempts = 5 if difficulty_level == "hard" else 10
game(attempts)

"""
Welcome to the Number Guessing Game!
I'm thinking of a number between 1 and 100.
Choose a difficulty. Type 'easy' or 'hard': hard
You have 5 attempts remaining to guess the number.
Make a guess: 55
Too high.
Guess again.
You have 4 attempts remaining to guess the number.
Make a guess: 23
You got it! The answer was 23.
"""