import random

def guess_number():
    secret_number = random.randint(1, 100)
    while True:
        try:
            guess = int(input("Guess the number between 1 and 100: "))
            if guess < 1 or guess > 100:
                print("Please enter a number between 1 and 100.")
            elif guess < secret_number:
                print("Too low! Try again.")
            elif guess > secret_number:
                print("Too high! Try again.")
            else:
                print("Congratulations! You guessed the correct number:", secret_number)
                break
        except ValueError:
            print("Invalid input! Please enter a valid number.")

guess_number()