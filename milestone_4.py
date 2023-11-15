# Milestone 4:
import random
word_list = ["apple", "banana", "orange", "pear", "mango"]

class Hangman:

      def __init__(self, word_list, num_lives=5):
          self.word_list = word_list
          self. num_lives = num_lives
          self.word = random.choice(word_list)
          self.user_guessed = ["_"] *len(self.word)
          self.list_of_guesses = []
          self.num_letters = len(self.word)

          print(list(map(lambda x: x.lower(), word_list)))

      def check_guess(self, guess):

          if guess in list(self.word):
           print("Good guess! {guess} is in the word.")
           self.num_letters -= 1
          else:
           self.num_lives -= 1
           indices = [i for i, guess in enumerate(self.word) if guess == self.user_guessed]
          for i, L in enumerate(self.word):
            if L == guess:
                self.user_guessed[i]= L
            elif guess != self.user_guessed:
              print("guess, is not the the letter")
              self.num_letters -= 1
            else:
                self.num_lives -=1
                print(f"The letter guessed is wrong,you have :  {self.num_lives} lives left")
                if self.num_lives == 0:
                   print(f"The word is : {self.word}")
                   print(f"You lost")
                break
                self.ask_letter()
            break
          pass
      def ask_for_input(self):

          while True:
           guess = input("Enter the single Letter: ").lower()
           if len(self.word)  != 1 and not guess.isalpha():
             print("Invalid letter. Please, enter a single alphabetical character.")
             self.list_of_guesses.append(guess)
             continue
           elif guess in self.list_of_guesses:
             print("You already tried that letter!", guess)
             continue
           else:
              print(self.word)
              break
              self.check_guess()
           break

hangaman = Hangman(word_list, num_lives=5)
Hangman.ask_letter()
Hangman.check_letter()
