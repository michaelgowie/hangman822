import random as ran

possible_word_list = ['Banana', 'Kiwi', 'Raspberry', 'Avocado', 'Nectarine', 'Apple', 'Peach', 'Mango', 'Strawberry']


class Hangman:
    '''
    This class facilitates the playing of the game hangman. An instance of this class represents a gae of hangman.

    Attributes:
        word (str): this is the word the user is trying to guess.
        word_guessed (list): what the user is shown during playing, contains underscores where unguessed letters are and guessed letters.
        num_letters (int): the number of remianing letters to guess.
        num_lives (int): the number of lives the player has remaining.
        word_list (list): the list of words the computer randomly chooses from.
        list_of_guesses: a list which contains all guesses the player has made.
    
    '''
    def __init__(self, word_list, num_lives  = 5):
        '''
        This chooses the random word, formulates the word_guessed list per the length of the word sets the attributes to their start values.
        '''
        self.word = ran.choice(word_list).lower()
        self.word_guessed = ['_' for i in range(len(self.word))]
        self.num_letters = len(set(list(self.word)))
        self.num_lives = num_lives
        self.word_list = word_list
        self.list_of_guesses = []
    def check_guess(self, letter):
        '''
        This method dictates what is done to the game state after a specific guess.

        If the letter is correct, the num_letters variable is updated and the letter is placed into the word_guessed list in the correct place(s). 
        If incorrect, the number of lives is reduced by one. In either case, information avout the success of the guess is printed.  
        '''
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
        '''
        This method obtains a letter from the user to guess.

        The method will only accept a single chracter which is in th ealphabet and has not been guessed previously. If these aren't met, the method will ask the user for a different input.
        '''
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
        '''
        This method obtains a list of indices which a certain letter appears in the word to be guessed.
        '''
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


