import random

class Hangman:

      def __init__(self, word_list, num_lives=5):
          self.word_list = word_list
          self. num_lives = num_lives
          self.word = random.choice(word_list)
          self.word_guessed = ["_"] *len(self.word)
          self.list_of_guesses = []
          self.num_letters = len(self.word)

          print(list(map(lambda x: x.lower(), word_list)))
          print(f"The mistery word has {self.num_letters} characters")
          print(f"{self.word_guessed}")

      def check_letter(self, letter) -> None:
          '''
        Checks if the letter is in the word.
        If it is, it replaces the '_' in the word_guessed list with the letter.
        If it is not, it reduces the number of lives by 1.
        Parameters:
        ----------
        letter: str
            The letter to be checked
          '''
          if letter in list(self.word):
             print(f"Yes: {letter} is in the word")
             
             indices = [i for i, letter in enumerate(self.word) if letter == self.word_guessed]
             for i, L in enumerate(self.word):
                if L == letter:
                  self.word_guessed[i] = L
                  print(f"Your word so far is: {self.word_guessed}")
                  self.num_letters -= 1
                  self.list_of_guesses.append(letter)
          else:
            self.num_lives -= 1
            print(f"Sorry! The letter {letter} is not in the word")
            print(f"You have {self.num_lives} lives left")
            pass
      def ask_letter(self):
        '''
        Asks the user for a letter and checks two things:
        1. If the letter has already been tried
        2. If the character is a single character
        If it passes both checks, it calls the check_letter method.
        '''
        while True:
            letter =input("Enter a single letter: ").lower()
            if len(letter) != 1:
              print(f"Oops Invalid! Please enter just one character:") 
                      
              continue
            elif letter in self.list_of_guesses:
                 print(f"{letter}  was already tried")
                 self.list_of_guesses.append(letter)
            else:
              self.check_letter(letter)
            break
        return letter
      pass
def play_game(worl_list):

    game = Hangman(word_list, num_lives=5)
    game.ask_letter()
    while True:
        if game.num_lives == 0:
           print("You lost!")
           print(f"The mystery word was:", game.word)
           print(game.num_letters)
           break
        elif game.num_letters > 0:
             game.ask_letter()       
        if game.num_lives != 0 and game.num_letters == 0:
           print("Congratulations. You won the game!")
           break
if __name__ == "__main__":
   word_list = ["apple", "banana", "orange", "pear", "mango"]
   play_game(word_list)
   word = random.choice(word_list)
   num_letters = len(word)
