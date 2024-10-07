import random as ran
def choose_random_word():
    possible_word_list = ['Banana', 'Kiwi', 'Raspberry', 'Avocado', 'Nectarine', 'Apple', 'Peach', 'Mango', 'Strawberry']

    word_to_guess = ran.choice(possible_word_list)
    return word_to_guess




