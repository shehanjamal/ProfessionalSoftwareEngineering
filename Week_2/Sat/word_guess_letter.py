import random

def generate_word():
    words_list_ = ["king", "", "spade", "jack", "ace", "joker", "heart", "deck", "club", "red", "black","white", "blue", "orange", "purple", "pink"]
    return random.choice(words_list_)

def check_letter(word_):
    guess_count_ = len(word_) + 3
    count_ = guess_count_
    guess_ = ["_"] * len(word_)
    for i in range(guess_count_):
        count_ -= 1
        print('You have', count_, 'to guess the word:')

        user_input_ = input('Guess the letter: ')

        letter_ = user_input_.lower()

        if validations(letter_):
            guess_count_ += 1
            continue


        if letter_ in word_:

            position = word_.index(letter_)
            guess_[position] = letter_
            print('Correct')
        else:
            print('Incorrect, try again')

        print('Current guess:', *guess_, sep=' ')

        end_game_ = end_game(guess_, count_, word_)
        if end_game_:
            break

        print(' ')

def end_game(guess_, count_, word_):
    if "_" not in guess_:
        print('Congratulations! You guessed the word:', word_)
        return True 
    if count_ == 0:
        print('You have no more guesses left. The word was:', word_)
        return True

def validations(letter_):
        if len(letter_) != 1:
            print('Please enter a single letter.')
            return True
        else:
            return False

if __name__ == "__main__":
   word_ = generate_word()

   letter_count_ = len(word_)
   print('Word length:',' _ '* letter_count_)
   check_letter(word_)
