import random

word_list = ['Apple', 'Banana', 'Orange', 'Mango', 'Pear']
word=random.choice(word_list)
print(word.lower())

guess = input("Enter a Single Letter:")

guess_length = len(guess)
print(guess_length)
# Check if the input is a single letter and alphabetical
if guess_length == 1 and guess.isalpha():
    # Do something if the condition is true
    print("Good Guess!")
else:
    # Do something else if the condition is false
    print("Oops! That is not a valid input." )
