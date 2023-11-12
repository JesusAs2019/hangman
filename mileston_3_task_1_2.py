import random

word_list = ['Apple', 'Banana', 'Orange', 'Mango', 'Pear']
print(list(map(lambda x: x.lower(), word_list)))
word = random.choice(word_list)


# Step 1:
# Create a while loop and set the condition to True. Setting the condition to True ensures that the code runs continuously.
while True:
# In the body of the loop, write the code required for the following steps.
# Step 2:
# Ask the user to guess a letter and assign this to a variable called guess.
      guess = input("Enter a Single Letter:")
# Step 3:
# Check that the guess is a single alphabetical character. Hint: You can use Python's isalpha method to check if the guess is alphabetical.
      guess_length = len(guess)
      print(guess_length)
      if guess in word and guess.isalpha():
         if guess_length == 1 and guess.isalpha():
# Step 4:
# If the guess passes the checks, break out of the loop.
             print("Good Guess")
             print(word.lower())
             break
      else:
# Step 5:
# If the guess does not pass the checks, then print a message saying "Invalid letter. Please, enter a single alphabetical character." else:
       print("Invalid letter. Please, enter a single alphabetical character.",)
   # Check whether the letter guessed by the user is in the secret word that was randomly chosen by the computer.
#For example, if the user guesses the letter "a" and the secret word is "apple", then your code should check if "a" is in "apple".
#Step 1:
#Create an if statement that checks if the guess is in the word.
      if guess in word:
# Step 2:
# In the body of the if statement, print a message saying "Good guess! {guess} is in the word.". Obviously, format the string to show the actual guess instead of {guess}.
        print("Good guess!", {guess} , "is in the word.")
        print(word.lower())
        break
# Step 3:
# Create an else block that prints a message saying "Sorry, {guess} is not in the word. Try again." This block of code will run if the guess is not in the word.
      else:
          print("Sorry!", {guess}, "is not in the word. Try again.")