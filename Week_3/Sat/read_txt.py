class ReadWriteTxt:
    def __init__(self, txt_add, filename):
        self.text_add = txt_add
        self.filename = filename

    def read_txt(self):
        with open(self.filename, "r", encoding="utf-8") as file:
            content = file.readlines()
            for line in content:
                print(line)

    def write_txt(self):
        with open(self.filename, "a") as file:
            file.write(self.text_add)



def main():
    read_write = ReadWriteTxt("This is an addition done by user.\n", "demo.txt")
    read_write.read_txt()
    read_write.write_txt()

if __name__ == "__main__":
    main()