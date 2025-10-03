from random import randint
# import maths


def my_function():
    for i in range(1, 21):
        if i == 20:
            print(f"You got it!")

# Describe the problem - Write your answers as comments:
# 1. what is the loop doing?
# 2. When is the function meant to print "You got it!"?
# 3. What are your assumptions about the value of i?


def print_dice():
    dice_images = ["1", "2", "3", "4", "5", "6"]
    dice_num = randint(1, 6)
    print(dice_images[dice_num-1])


def print_your_year_of_birth():
    year = int(input("What is your year of birth?"))

    if year > 1980 and year <= 1994:
        print(f"You are a Millennial")
    elif year > 1994:
        print("You are a Gen Z")


def tell_if_you_can_drive():
    age = int(input("How old are you?"))
    if age > 18:
        print("You can drive at age {age}.")


def count_total_words():
    word_per_page = 0
    pages = int(input("Number of pages: "))
    word_per_page = int(input("Number of words per page: "))
    total_words = pages * word_per_page

    print(f"We have {total_words} in total.")



def mutate(a_list):
    b_list = []
    new_item = 0
    for item in a_list:
        new_item = item * 2
        new_item += randint(1, 3)
        new_item = maths.add(new_item, item)
    b_list.append(new_item)

    print(b_list)


if __name__ == "__main__":
    # example 1
    #Soulution 1 i creased the range to 21 so that it includes 20
    #Soulution 2 Chabge the if staement to make it stop at 19 since 20 is not included.
    my_function()

    # example 2
    #Soulution from 1 to 6 but list starts from 0 so reduce the randint by 1
    print_dice()

    # example 3
    #solution year 1994 is not covered in the if statement so added = to the 1994
    print_your_year_of_birth()

    # example 4
    #solution is to remove = because == is for checking equality not assignment
    count_total_words()

    # example 5
    a_demo_list = [1, 2, 3, 4, 5, 6, 7]
    mutate(a_demo_list)