class ReadWriteTxt:
    def __init__(self, filename):
        self.filename = filename

    def count_word(self):
        with open(self.filename, "r", encoding="utf-8") as file:
            content = file.readlines()
            count = 0
            for line in content:
                count += len(line.split())
            print("Total word count:", count)


def main():
    read_write = ReadWriteTxt("demo.txt")
    read_write.count_word()

if __name__ == "__main__":
    main()