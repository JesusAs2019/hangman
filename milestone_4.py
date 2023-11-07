# Milestone 4:
import random

class Hangman:

    def _init_(self, word_list, num_lives=5):
        self.word = random.choice(word_list)
        self.user_guessed = "_" *len(self.word)
        self.num_letters = 0
        self.num_lives = 5
        self.list_of_guesses = [] 
        self.word_list = ['Apple', 'Banana', 'Orange', 'Mango', 'Pear']
        
        print(list(map(lambda x: x.lower(), word_list)))
        print(random.choice(word_list))  
    def check_guess(self):
        self.guess.lower()
        if self.guess in self.word:
          print("Good guess! {guess} is in the word.")
          num_letters -= 1
          indices = [i for i, letter in enumerate(word) if letter == guess]
        else:
           num_lives -= 1 
        for index in indices:
              if letter == guess:
               self.user_guessed[index]= guess      
              elif letter != guess:
                 print("guess, is not the the letter")
        num_letters -= 1 
        def ask_for_input(self):
               while True:
                 guess = input("Enter the single Letter: ")      
                 if guess != 1 and not guess.isalpha():
                  print("Invalid letter. Please, enter a single alphabetical character.")
                 elif guess in self.list_of_guesses:
                  print("You already tried that letter!", guess)
                 else:
                   return self.check_guess(guess)
        list_of_guesses.append(guess)
         
        ask_for_input()
    check_guess(self)  
            
    if __name__=="__main__":
      word_list = ['Apple', 'Banana', 'Orange', 'Mango', 'Pear']
      game = hangman(guess)
      