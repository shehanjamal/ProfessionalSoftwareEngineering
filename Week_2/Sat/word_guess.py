import random

def generate_word():
    words_list_ = ["king", "spade", "jack", "ace", "joker", "heart", "deck", "club", "red", "black","white", "blue", "orange", "purple", "pink"]
    return random.choice(words_list_)

def guess_letter(word_):
    guess_count_ = len(word_) + 3
    count_ = guess_count_
    guess_ = ["_"] * len(word_)
    while guess_count_ > 0:
        count_ -= 1
        print('You have', count_, 'to guess the word:')

        user_input_ = input('Guess the letter: ')

        letter_ = user_input_.lower()

        if validations(letter_):
            guess_count_ += 1
            count_ += 1
            continue


        if letter_ in word_:

            position = word_.index(letter_)
            guess_[position] = letter_
            guess_count_ += 1
            count_ += 1
            print('Correct')
        else:
            print('Incorrect, try again')

        print('Current guess:', *guess_, sep=' ')

        end_game_ = end_game(guess_, count_, word_)
        if end_game_:
            break

        print(' ')
        
def guess_word_(word_):
    guess_count_ = len(word_) + 3
    count_ = guess_count_
    guess_ = ["_"] * len(word_)
    while guess_count_ > 0:
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

def validations(letter_):
        if len(letter_) != 1:
            print('Please enter a single letter.')
            return True
        else:
            return False

if __name__ == "__main__":
   difficulty = input("Choose mode number(1 : Letter, 2: Word): ")
   word_ = generate_word()

   letter_count_ = len(word_)
   print('Word length:',' _ '* letter_count_)
   print(' ')
   
   if difficulty == '1':
        guess_letter(word_)
   elif difficulty == '2':
        guess_word_(word_)
   else:
        print("Invalid mode selected. Please choose 1 or 2.")   