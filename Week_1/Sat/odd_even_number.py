def even_number():
    number = input("Enter a number: ")
    x = int(number)
    if x>= 0:
        # z=1
        # for i in range(1, x + 1):
        #    if i % 2 == 0:
        #        print(i)
        #        z += i
        # return z - 1
        i = 1
        z = 1
        while i <= x:
            if i % 2 == 0:
                print(i)
                z += i
            i += 1
        return z - 1
    else:
        return 'enter greater than 0'
    
def odd_number():
    number = input("Enter a number: ")
    x = int(number)
    if x>= 0:
        # z=1
        # for i in range(1, x + 1):
        #    if i % 2 == 0:
        #        y=0
        #    else:
        #        print(i)
        #        z += i
        # return z - 1
        i = 1
        z = 1
        while i <= x:
            if i % 2 == 0:
                pass
            else:
                print(i)
                z += i
            i += 1
        return z - 1
    else:
        return 'enter greater than 0'




if __name__ == "__main__":
    ans_1 = even_number()
    ans_2 = odd_number()
    print("final result even:", ans_1)
    print("final result odd:", ans_2)