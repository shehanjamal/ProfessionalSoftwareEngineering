def read_txt():
    with open("demo.txt", "r", encoding="utf-8") as file:
        content = file.readlines()
        for line in content:
            print(line)

def write_txt():
    with open("demo.txt", "a") as file:
        file.write("This is as addition done by user.\n")

def main():
    read_txt()
    write_txt()
    
if __name__ == "__main__":
    main()