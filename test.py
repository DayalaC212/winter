#This is a test
def count_letters(sentence):
    # Initialize an empty dictionary to store letter counts
    letter_counts = {}

    # Iterate through each character in the sentence
    for char in sentence:
        # Check if the character is a letter
        if char.isalpha():
            # Convert the letter to lowercase for case-insensitive counting
            char = char.lower()

            # Update the count in the dictionary
            letter_counts[char] = letter_counts.get(char, 0) + 1

    return letter_counts

# Example usage
input_sentence = "Hello, World!"
result = count_letters(input_sentence)

# Display the result
for letter, count in result.items():
    print(f"{letter}: {count}")
