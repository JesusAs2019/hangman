## Good job so far!
# But your code probably doesn't look great.
# It's hard to tell which lines do what.
# Create 2 functions, check_guess and ask_for_input functions which contain the code for those two things.

## The check_guess function will take the guessed letter as an argument and check if the letter is in the word.

import random

# Step 1:
# Define a function called check_guess. pass in the guess as a parameter for the function.
def check_guess(guess):

    word_list = ['Apple', 'Banana', 'Orange', 'Mango', 'Pear']
    print(list(map(lambda x: x.lower(), word_list)))
    word = random.choice(word_list)
    guessed_list = guess
    print(word)
## Write the code for the following steps in the body of this function.
# Step 2:
# Convert the guess into lower case.
    guess = guess.lower()
    print(guess)
# Step 3:
# Move the code that you wrote to check if the guess is in the word into this function block.
if guess in word:
      # Step a:
   # In the body of the if statement, print a message saying "Good guess! {guess} is in the word.". Obviously, format the string to show the actual guess instead of {guess}.
        print("Good guess!", guess , "is in the word.")
      # Step b:
   # Create an else block that prints a message saying "Sorry, {guess} is not in the word. Try again." This block of code will run if the guess is not in the word.
else:
          print("Sorry!", {guess}, "is not in the word. Try again.")
# The ask_for_input function.
# Step 1:
# Define a function called ask_for_input.
def ask_for_input():
# Step 2:
# over the code that you wrote in the Iteratively check if the input is a valid guess task into this function block.
    # Create a while loop and set the condition to True. Setting the condition to True ensures that the code runs continuously.
      while True:
# In the body of the loop, write the code required for the following steps
    # Step a:
# Ask the user to guess a letter and assign this to a variable called guess.
        guess = input("Enter a Single Letter:")
        
    # Step b:
# Check that the guess is a single alphabetical character. Hint: You can use Python's isalpha method to check if the guess is alphabetical.
        guess_length = len(guess)
        print(guess_length)
        
        if guess_length == 1 and guess.isalpha():
          # Step c:
# If the guess passes the checks, break out of the loop.
             break
        else:
    # Step d:
# If the guess does not pass the checks, then print a message saying "Invalid letter. Please, enter a single alphabetical character." else:
         print("Invalid letter. Please, enter a single alphabetical character.",)
# Step 3:
# Outside the while loop, but within this function, call the check_guess function to check if the guess is in the word. Don't forget to pass in the guess as an argument to the method.
# Step 4:
# outside the function, call the ask_for_input function to test your code.   
check_guess(guess)
ask_for_input()