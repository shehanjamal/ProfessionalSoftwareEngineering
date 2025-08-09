class StringManipulation:
    def __init__(self, text):
        self.text = text

    def find_character(self, char):
        return self.text.find(char)
    
    def find_length(self):
        return len(self.text)
    
    def convert_uppercase(self):
        return self.text.upper()
    
if __name__ == "__main__":
    name = StringManipulation("example")

    print("Original Text: ", name.text)  # Output: example

    result_char = name.find_character("x")
    print("Find Characther: ",result_char)  # Output: 1

    result_len = name.find_length()
    print("Find Length: ",result_len)  # Output: 7

    result_upper = name.convert_uppercase()
    print("Convert Uppercase: ",result_upper)  # Output: EXAMPLE