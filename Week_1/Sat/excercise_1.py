def average():
    number1 = input("Enter a number to find num 1: ")
    number2 = input("Enter a number to find num 2: ")
    number3 = input("Enter a number to find num 3: ")

    avg = (float(number1) + float(number2) + float(number3)) / 3
    return avg


if __name__ == "__main__":
    ans = average()
    print("final result:", ans)