class StringManipulation:
    def __init__(self, sentence):
        self.sentence = sentence

    def find_text_length(self):
        return self.sentence.split()  
    
    
if __name__ == "__main__":
    sentence = input("Enter a sentence: ")

    name = StringManipulation(sentence)

    print("Original Text: ", name.sentence)  # Output: example

    res_sentence = name.find_text_length()
    # Spltting the words into a list so that the words can be counted
    print("Split words: ", res_sentence)  # Output: ['This', 'is', 'a', 'sample', 'sentence', 'for', 'testing']
    #getting the length of the list we split
    print("Count words: ", len(res_sentence))  # Output: 7

