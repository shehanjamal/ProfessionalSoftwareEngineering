def factorial():
    number = input("Enter a number to find factorial: ")
    x = int(number)
    if x>= 1:
        z=1
        for i in range(1, x + 1):
           z *= i
        return z
    elif x == 0:
        return 1
    else:
        return 'enter greater than 0'


if __name__ == "__main__":
    ans = factorial()
    print("final result:", ans)