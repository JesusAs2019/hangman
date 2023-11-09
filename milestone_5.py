import random

class Hangman:

      def __init__(self, word_list, num_lives=5):
          self.word = random.choice(word_list)
          self.word_guessed = ["_"] *len(self.word)
          self.num_letters = len(set(self.word))
          self.num_lives = 6
          self.word_list = ['Apple', 'Banana', 'Orange', 'Mango', 'Pear']
          self.list_of_guesses = []
          self.letter = self.list_of_guesses
          print(list(map(lambda x: x.lower(), word_list)))
          print(f"This is the mistery word has {self.num_letters} characters")
          print(f"{self.word_guessed}")

      def check_letter(self, letter) -> None:
        for i, L in enumerate(self.word):
            if L == letter:
             self.word_guessed[i] = L
             print(f"Yes {letter} is in the word")
             print(f"Your word so far : {self.word_guessed}")
        '''
        Checks if the letter is in the word.
        If it is, it replaces the '_' in the word_guessed list with the letter.
        If it is not, it reduces the number of lives by 1.
        Parameters:
        ----------
        letter: str
            The letter to be checked
        '''
        if letter in self.word:
          letter.lower()
          self.list_of_guesses.append(letter)
          self.num_letters -= 1
        elif letter not in self.word:
         self.list_of_guesses.append(letter)
         self.num_lives -= 1
        for i, L in enumerate(self.word):
           if L == letter:
              self.word_guessed[i] = L
        pass
      def ask_letter(self):
        '''
        Asks the user for a letter and checks two things:
        1. If the letter has already been tried
        2. If the character is a single character
        If it passes both checks, it calls the check_letter method.
        '''
        while True:
            letter =input("Enter a letter: ").lower()
            if len(letter) != 1:
                    print(f"Enter just one character: ")
                    continue
            elif letter in self.list_of_guesses:
                    print(f"{letter}  was already tried")
                    self.list_letter.append(letter)
                    continue
            else:
              self.check_letter(letter)
            break     
      pass
def play_game(word_list):       
    num_lives = 6
    game = Hangman(word_list, num_lives=5)
    game.ask_letter()
    while True:
        if game.num_lives == 0:
           print("You lost! The word was: {word")
        elif game.num_letters > 0:
         return game.ask_letter()
        continue
        if game.num_lives != 0 and not game.num_letters > 0:
           print('Congratulations. You won the game!')
        else:
         pass
         
if __name__ == '__main__':
   word_list = ['apple', 'banana', 'orange', 'pear', 'mango']
play_game(word_list)