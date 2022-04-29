

import requests


class RandomWords:
    """Get random words, in spanish language."""
    def __init__(self):
        """Class constructor."""
        url = 'https://clientes.api.greenborn.com.ar/public-random-word'
        response = requests.request('get', url)
        self.word = response.text[2:-2]

    def get_word(self) -> str:
        """Returns the generated random word."""
        return self.word


class Boards:
    """Manage game boards, based on a word."""
    def __init__(self, word: str):
        """Class constructor.

        Params:
            - word: str expected, random generated word, to generate the boards.
        """
        self.word = word
        self.word_length = len(self.word)
        base_character = '_ '
        white_board = self.word_length * base_character
        self.white_board = white_board[:-1]

    def get_white_board(self) -> str:
        """Returns a board with underscores instead of letters."""
        return self.white_board

    def get_full_board(self) -> str:
        """Returns the full board, in uppercase format."""
        full_board = ''.join(list(map(lambda x: x.upper() + ' ', self.word)))[:-1]
        return full_board


class Hangman:
    """Full Hangman game mechanics."""
    def __init__(self):
        self.word = RandomWords().get_word().upper()
        self.white_board = Boards(word=self.word).get_white_board()
        self.full_board = Boards(word=self.word).get_full_board()
        self.turns_left = 6
        self.words_used = []

    def start_game(self):
        """Start a new Hangman game."""
        print('Welcome to Hangman game.')
        print('This is the word that you must guess:')
        print(self.white_board)
        self.new_turn(current_board=self.white_board)

    def new_turn(self, current_board: str):
        """Starts a new turn."""
        if self.turns_left > 0:
            print(f'Turns left: {self.turns_left}')
            print(current_board)
            user_letter = input("It's your turn, write a letter...").upper()
            was_used = self.evaluate_used_letters(letter=user_letter)
            if was_used:
                self.call_new_turn(current_board=current_board, subtract_turn=False)
            else:
                letter_on_word = self.evaluate_letter_on_word(letter=user_letter)
                if letter_on_word:
                    current_board = self.modify_board(user_letter=user_letter, current_board=current_board)
                    print(f'The letter {user_letter} is in the word!')
                    self.call_new_turn(current_board=current_board, subtract_turn=False)
                else:
                    print(f'Sorry, the letter {user_letter} is not in the word.')
                    self.call_new_turn(current_board=current_board, subtract_turn=True)
        else:
            self.game_over(win=False)

    def evaluate_letter_on_word(self, letter: str) -> bool:
        """Evaluates whether the received letter exists on self.word or not."""
        letter_on_word = letter.upper() in self.word
        return letter_on_word

    def modify_board(self, user_letter: str, current_board: str) -> str:
        """Modify the received Board with the received letter,
        based on the position of the letter in self.word.
        """
        updated_board = ''
        for position, character in enumerate(self.full_board):
            if character != user_letter.upper():
                updated_board += current_board[position]
            else:
                updated_board += user_letter
        return updated_board

    def call_new_turn(self, current_board: str, subtract_turn: bool):
        """Calls self.new_turn method, to avoid recursion. Subtract one turn left before
        calling the function, if 'subtract_turn' is True.
        """
        if '_' not in current_board:
            self.game_over(win=True)
            return
        if subtract_turn:
            self.turns_left -= 1
        self.new_turn(current_board=current_board)

    def evaluate_used_letters(self, letter: str) -> bool:
        """Evaluates if the received letter by parameter was already used by the user.

        Params:
            - letter: str expected, letter to evaluate.
        Return:
            - Bool: False if the letter was not used, True if it was.
        """
        was_used = letter in self.words_used
        if was_used:
            print('Letter was already used.')
            return True
        self.words_used.append(letter)
        return False

    def game_over(self, win: bool):
        """Close the game; 'win' parameter indicates whether the user won or lost.
        The 'current_board' parameter is used to show the user the requested word.
        """
        if win:
            print('Congratulations, you won !!')
            print(self.full_board)
        else:
            print('Sorry, you lose !! The word was:')
            print(self.full_board)


if __name__ == "__main__":
    Hangman().start_game()






