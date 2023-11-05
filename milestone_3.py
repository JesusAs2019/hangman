import random

word_list = ['Apple', 'Banana', 'Orange', 'Mango', 'Pear']
print(list(map(lambda x: x.lower(), word_list)))
word = random.choice(word_list)
print(word.lower())


          