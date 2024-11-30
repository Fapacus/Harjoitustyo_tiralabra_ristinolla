import unittest
import xoxo


class TestXoxo(unittest.TestCase):
    def setUp(self):
        pass

    def test_win_row(self):
        board = [
            [" ", " ", " ", " ", " ", " "],
            ["X", "X", "X", "X", "X", " "],
            [" ", " ", " ", " ", " ", " "],
            [" ", " ", " ", " ", " ", " "],
            [" ", " ", " ", " ", " ", " "],
            [" ", " ", " ", " ", " ", " "]
        ]
        last_move = (1, 2)
        self.assertTrue(xoxo.win_win(board, last_move))

        board = [
            [" ", " ", " ", " ", " ", " "],
            [" ", "X", "X", "X", "X", " "],
            [" ", " ", " ", " ", " ", " "],
            [" ", " ", " ", " ", " ", " "],
            [" ", " ", " ", " ", " ", " "],
            [" ", " ", " ", " ", " ", " "]
        ]
        last_move = (1, 2)
        self.assertFalse(xoxo.win_win(board, last_move))

    def test_win_column(self):
        board = [
            [" ", " ", " ", " ", " ", " "],
            [" ", " ", " ", "X", " ", " "],
            [" ", " ", " ", "X", " ", " "],
            [" ", " ", " ", "X", " ", " "],
            [" ", " ", " ", "X", " ", " "],
            [" ", " ", " ", "X", " ", " "]
        ]
        last_move = (1, 3)
        self.assertTrue(xoxo.win_win(board, last_move))

    def test_win_column(self):
        board = [
            [" ", " ", " ", " ", " ", " "],
            [" ", " ", " ", "X", " ", " "],
            [" ", " ", " ", "X", " ", " "],
            [" ", " ", " ", "X", " ", " "],
            [" ", " ", " ", " ", " ", " "],
            [" ", " ", " ", "X", " ", " "]
        ]
        last_move = (3, 3)
        self.assertFalse(xoxo.win_win(board, last_move))

    def test_win_diagonal(self):
        board = [
            [" ", " ", " ", " ", " ", " "],
            [" ", "X", " ", "X", " ", " "],
            [" ", " ", "X", "X", " ", " "],
            [" ", " ", " ", "X", " ", " "],
            [" ", " ", " ", " ", "X", " "],
            [" ", " ", " ", " ", " ", "X"]
        ]
        last_move = (1, 1)
        self.assertTrue(xoxo.win_win(board, last_move))
    
    def test_win_diagonal(self):
        board = [
            [" ", " ", " ", " ", " ", " "],
            [" ", "X", " ", "X", " ", " "],
            [" ", " ", "X", "X", " ", " "],
            [" ", " ", " ", " ", " ", " "],
            [" ", " ", " ", " ", "X", " "],
            [" ", " ", " ", " ", " ", "X"]
        ]
        last_move = (5, 5)
        self.assertFalse(xoxo.win_win(board, last_move))

    def test_win_diagonal(self):
        board = [
            [" ", " ", " ", " ", " ", "X"],
            [" ", "X", " ", "X", "X", " "],
            [" ", " ", "X", "X", " ", " "],
            [" ", " ", "X", " ", " ", " "],
            [" ", "X", " ", " ", "X", " "],
            [" ", " ", " ", " ", " ", "X"]
        ]
        last_move = (4, 1)
        self.assertTrue(xoxo.win_win(board, last_move))

    def test_win_diagonal(self):
        board = [
            [" ", " ", " ", " ", " ", "X"],
            [" ", "X", " ", "X", "X", " "],
            [" ", " ", "X", "O", " ", " "],
            [" ", " ", "X", " ", " ", " "],
            [" ", "X", " ", " ", "X", " "],
            [" ", " ", " ", " ", " ", "X"]
        ]
        last_move = (2, 3)
        self.assertFalse(xoxo.win_win(board, last_move))