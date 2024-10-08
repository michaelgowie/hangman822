import random as ran
def choose_random_word():
    possible_word_list = ['Banana', 'Kiwi', 'Raspberry', 'Avocado', 'Nectarine', 'Apple', 'Peach', 'Mango', 'Strawberry']

    word_to_guess = ran.choice(possible_word_list)
    return word_to_guess




stringdr = 'iqfoijqwcksdkajslkqeckelialkaej'

letter = 'q'
curr_idx = -1
list_of_ids = []
x = 0
while x < 10:
    if letter in stringdr[curr_idx + 1:]:
        print(stringdr.find(letter, curr_idx + 1))
        print(stringdr[curr_idx + 1:])
        curr_idx = stringdr.find(letter, curr_idx + 1)
        list_of_ids.append(curr_idx)
        
        
        x += 1
    else: 
        break
for idx in list_of_ids:
    print(stringdr[idx])