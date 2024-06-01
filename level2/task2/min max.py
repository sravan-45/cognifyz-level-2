import random

def guess_number(min_num, max_num):
    secret_number = random.randint(min_num, max_num)
    while True:
        try:
            guess = int(input(f"Guess the number between {min_num} and {max_num}: "))
            if guess < min_num or guess > max_num:
                print(f"Please enter a number between {min_num} and {max_num}.")
            elif guess < secret_number:
                print("Too low! Try again.")
            elif guess > secret_number:
                print("Too high! Try again.")
            else:
                print("Congratulations! You guessed the correct number:", secret_number)
                break
        except ValueError:
            print("Invalid input! Please enter a valid number.")

# Prompt the user to enter the range
while True:
    try:
        min_range = int(input("Enter the minimum number for the range: "))
        max_range = int(input("Enter the maximum number for the range: "))
        break
    except ValueError:
        print("Invalid input! Please enter integer values for the range.")

# Call the function with the specified range
guess_number(min_range,max_range)
