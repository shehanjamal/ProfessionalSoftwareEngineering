"""A simple command-line Tic Tac Toe game for two players."""
class User:
    """Class to represent a player in the game."""
    def __init__(self, name, symbol):
        """Initialize user with a name and symbol (X or O)."""
        self.name = name
        self.symbol = symbol

    def get_name(self):
        """Return the name of the user."""
        return self.name

    def get_symbol(self):
        """Return the symbol of the user."""
        return self.symbol

class Game:
    """Class to manage the Tic Tac Toe game logic."""
    def __init__(self, user1, user2):
        """Initialize the game with two users and an empty board."""
        self.board = [' ' + str(i) + ' ' for i in range(9)]
        self.current_user = user1
        self.user1 = user1
        self.user2 = user2

    def display_board(self):
        """Display the current state of the board."""
        print(self.board[0] + " | " + self.board[1] + " | " + self.board[2])
        print("----+-----+----")
        print(self.board[3] + " | " + self.board[4] + " | " + self.board[5])
        print("----+-----+----")
        print(self.board[6] + " | " + self.board[7] + " | " + self.board[8])

    def make_move(self, position):
        """Place the current user's symbol on the board at the given position."""
        if self.board[position] != 'X' and self.board[position] != 'O':
            self.board[position] = self.current_user.get_symbol()
            return True
        return False

    def check_winner(self):
        """Check if the current user has won the game and what the winning combination is."""
        winning_combinations = [
            (0, 1, 2), (3, 4, 5), (6, 7, 8),
            (0, 3, 6), (1, 4, 7), (2, 5, 8),
            (0, 4, 8), (2, 4, 6)
        ]
        for combo in winning_combinations:
            if self.board[combo[0]] == self.board[combo[1]] == self.board[combo[2]] != ' ':
                return True
        return False

    def switch_user(self):
        """Switch the current user to the other player."""
        self.current_user = self.user1 if self.current_user == self.user2 else self.user2

    def is_draw(self):
        """Check if the game is a draw."""
        return all(space in ['X', 'O'] for space in self.board)

def main():
    """Main function to run the Tic Tac Toe game."""
    player1_name = input("Enter the name for Player 1: ")
    user1 = User(player1_name, "X")
    player2_name = input("Enter the name for Player 2: ")
    user2 = User(player2_name, "O")
    game = Game(user1, user2)
    game.display_board()
    for _ in range(9):
        while True:
            try:
                position = int(input(game.current_user.get_name()+"'s turn "+
                                     "("+game.current_user.get_symbol()+"),choose position (0-8):"))
                if position < 0 or position > 8:
                    print("Invalid position. Choose a number between 0 and 8.")
                    continue
                if game.make_move(position):
                    break
                else:
                    print("Position already taken. Choose another.")
            except ValueError:
                print("Invalid input. Please enter a number between 0 and 8.")
        game.display_board()
        if game.check_winner():
            print(f"Congratulations {game.current_user.get_name()}! You win!")
            return
        game.switch_user()
        if game.is_draw():
            print("It's a draw!")
            return
if __name__ == "__main__":
    main()
