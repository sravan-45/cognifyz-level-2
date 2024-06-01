def generate_fibonacci_sequence(terms):
    fibonacci_sequence = [0, 1]  # Initialize the sequence with the first two terms

    # Generate the Fibonacci sequence
    for i in range(2, terms):
        next_term = fibonacci_sequence[-1] + fibonacci_sequence[-2]
        fibonacci_sequence.append(next_term)

    return fibonacci_sequence

# Take input from the user
try:
    num_terms = int(input("Enter the number of terms for the Fibonacci sequence: "))
    if num_terms <= 0:
        print("Please enter a positive integer.")
    else:
        fibonacci_sequence = generate_fibonacci_sequence(num_terms)
        print("Fibonacci sequence up to", num_terms, "terms:")
        print(fibonacci_sequence)
except ValueError:
    print("Invalid input! Please enter a valid integer.")