def is_palindrome(word):

    # Remove non-alphabetic characters and convert to lowercase
    word = ''.join(filter(str.isalpha, word)).lower()

    # Check if the word is equal to its reverse
    return word == word[::-1]


# Open the file containing English words
with open('dictionary.txt') as f:

    # Iterate over each line in the file
    for line in f:
        # Remove the newline character at the end of the line
        word = line.strip()
        # Check if the word is a palindrome
        if is_palindrome(word):
            print(word)
