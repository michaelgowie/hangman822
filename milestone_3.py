from milestone_2 import choose_random_word


def check_guess(letter):
    letter.lower()
    if letter in word_to_guess:
        print(f'Good guess, {letter} is in the word.')
    else:
        print(f'Unlucky, {letter} is not in the word')



def input_letter_guess():
    while True:
        user_guessed_letter = input('Guess a letter.')

        if len(user_guessed_letter) != 1 or user_guessed_letter.isalpha() == False:
            print('Please input exactly one letter') 
        else: 
            print('Good guess!')
            break
    check_guess(user_guessed_letter)
    return user_guessed_letter


answer_obtained = False
word_to_guess = choose_random_word()

input_letter_guess()






