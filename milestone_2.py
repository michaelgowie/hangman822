import random as ran

word_list = ['Banana', 'Kiwi', 'Raspberry', 'Avocado', 'Nectarine', 'Apple', 'Peach', 'Mango', 'Strawberry']

word = ran.choice(word_list)

guess = input('Guess a letter.')

if len(guess) != 1 or guess.isalpha() == False:
    print('Please input exactly one letter') 
