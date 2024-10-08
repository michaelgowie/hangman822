import random as ran

possible_word_list = ['Banana', 'Kiwi', 'Raspberry', 'Avocado', 'Nectarine', 'Apple', 'Peach', 'Mango', 'Strawberry']


class Hangman:
    def __init__(self, word_list, num_lives  = 5):
        self.word = ran.choice(word_list).lower()
        self.word_guessed = ['_' for i in range(len(self.word))]
        self.num_letters = len(set(list(self.word)))
        self.num_lives = num_lives
        self.word_list = word_list
        self.list_of_guesses = []
    def check_guess(self, letter):
        letter.lower()
        if letter in self.word:
            print(f'Good guess, {letter} is in the word.')
            letter_idx_list = self.get_letter_indices(letter)
            for idx in letter_idx_list:
                self.word_guessed[idx] = letter
            game.num_letters -= 1
        else:
            print(f'Unlucky, {letter} is not in the word')
            self.num_lives -= 1
            print(f'You have {self.num_lives} remaining.')
    def ask_for_input(self):
        while True:
            user_guessed_letter = input('Guess a letter.')

            if len(user_guessed_letter) != 1 or user_guessed_letter.isalpha() == False:
                print('Please input exactly one letter')
            elif user_guessed_letter in self.list_of_guesses:
                print(f'You already guessed {letter}! Guess something else.')
            else: 
                print('Good guess!')
                break
        self.check_guess(user_guessed_letter)
        self.list_of_guesses.append(user_guessed_letter)
    def get_letter_indices(self, letter):
        current_idx = 0
        list_of_indices = []
        while True:
            if letter in self.word[current_idx:]:
                list_of_indices.append(self.word.find(letter, current_idx))
                current_idx = self.word.find(letter, current_idx) + 1
            else:
                break
        return list_of_indices

        

game = Hangman(possible_word_list, 2)

print(game.word, game.word_guessed, game.num_letters, game.num_lives)

game.ask_for_input()

print(game.list_of_guesses)
print(game.word_guessed)


