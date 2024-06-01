import os
import string

def count_word_occurrences(file_path):
    word_counts = {}
    
    # Check if the file exists
    if not os.path.isfile(file_path):
        raise FileNotFoundError("File not found. Please enter a valid file path.")
    
    # Open the file and read its contents
    with open(file_path, 'r') as file:
        for line in file:
            # Split the line into words
            words = line.split()
            for word in words:
                # Remove punctuation marks and convert to lowercase
                word = word.strip(string.punctuation).lower()
                # Count occurrences of each word
                word_counts[word] = word_counts.get(word, 0) + 1
    
    # Sort the word counts alphabetically
    sorted_word_counts = sorted(word_counts.items())
    
    return sorted_word_counts

# Input the file path
file_path = input("Enter the path of the text file: ")

# Count word occurrences and display the results
try:
    word_occurrences = count_word_occurrences(file_path)
    for word, count in word_occurrences:
        print(f"{word}: {count}")
except FileNotFoundError as e:
    print(e)
except Exception as e:
    print("An error occurred:",e)