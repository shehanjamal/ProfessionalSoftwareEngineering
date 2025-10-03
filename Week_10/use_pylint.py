"""Module to demonstrate pylint usage with a class handling strings."""
class UseString:
    """A class to perform operations on strings or lists of strings."""
    def __init__(self, value):
        """Initialize with a string or list of strings."""
        self.value = value

    def calculate_length(self):
        """Calculate the length of the string or list of strings."""
        count = 0
        if isinstance(self.value, str):
            count = len(self.value)
        elif isinstance(self.value, list):
            for item in self.value:
                count += len(item)
        return count
    def count_uppercase(self):
        """Count the number of uppercase letters in the string."""
        count = 0
        for char in self.value:
            if char.isupper():
                count += 1
        return count

def main():
    """Main function to demonstrate UseString class functionality."""
    my_string = UseString("Hello")
    print("Length:", my_string.calculate_length())
    print("Uppercase Count:", my_string.count_uppercase())

    my_string2 = UseString(["Test", "Spade", "Heart", "Club", "Diamond"])
    print("Length:", my_string2.calculate_length())
    print("Uppercase Count:", my_string2.count_uppercase())

if __name__ == "__main__":
    main()
