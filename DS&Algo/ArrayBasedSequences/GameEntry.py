class GameEntry:
    """Represents one entry of a list of high scores"""
    def __init__(self,name,score):
        self._name=name
        self._score=score

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
        self._board=[None]*capacity
        self._n=0

    def __getitem__(self, k):
        """Return  the entry at index k"""
        return self._board[k]

    def __str__(self):
        """Return the string representation of the high score"""
