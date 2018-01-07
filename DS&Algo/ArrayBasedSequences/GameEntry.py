class GameEntry:
    """Represents one entry of a list of high scores"""

    def __init__(self, name, score):
        self._name = name
        self._score = score

    def get_name(self):
        return self._name

    def get_score(self):
        return self._score

    def __str__(self):
        return '({0}, {1})'.format(self._name, self._score)


class Scoreboard:
    """Fixed length sequences of high scores in non decreasing order"""

    def __init__(self, capacity=10):
        """Initialize the score board with the given capacity
        All entries are initially None"""
        self._board = [None] * capacity
        self._n = 0

    def __getitem__(self, k):
        """Return  the entry at index k"""
        return self._board[k]

    def __str__(self):
        """Return the string representation of the high score"""
        return '\n'.join(str(self._board[j]) for j in range(self._n))

    def add(self, entry):
        """Adding entries to the score board"""
        score = entry.get_score()
        # Does the new entry qualify as high score?
        # answer is yes if the board is not full or the score is higher than the last entry

        good = self._n < len(self._board) or score > self._board[-1].get_score()

        if good:
            if self._n < len(self._board):
                self._n += 1

            # shift the lower scores rightwards to make room for the new entry
            j = self._n - 1
            while j > 0 and self._board[j - 1].get_score() < score:
                self._board[j] = self._board[j - 1]
                j -= 1
            self._board[j] = entry
