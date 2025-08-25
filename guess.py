import random

print("Welcome to the Number Guessing Game!")
number_to_guess = random.randint(1, 100)
attempts = 0

while True:
    guess = input("Guess a number between 1 and 100 (or type 'exit' to quit): ")
    if guess.lower() == 'exit':
        print("Game exited. The number was:", number_to_guess)
        break
    try:
        guess = int(guess)
    except ValueError:
        print("Please enter a valid integer.")
        continue

    attempts += 1
    if guess < number_to_guess:
        print("Too low!")
    elif guess > number_to_guess:
        print("Too high!")
    else:
        print(f"Congratulations! You guessed the number in {attempts} attempts.")
        break
