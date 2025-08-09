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

        user_input_ = input('Guess the word: ')

        letter_ = user_input_.lower()
   
        incorrect_position = []
        for i in range(len(letter_)):

            if letter_[i] in word_:            
                position = word_.index(letter_[i])
                if i == position:
                    guess_[position] = letter_[i]
                else:
                    incorrect_position.append(letter_[i])
                    continue

 
        print('Letter in incorrect positions, try again:', incorrect_position)
            

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


if __name__ == "__main__":
   word_ = generate_word()

   letter_count_ = len(word_)
   print('Word length:',' _ '* letter_count_)
   check_letter(word_)
