import unittest
import xoxo
import heuristics


class TestXoxo(unittest.TestCase):
    def setUp(self):
        self.depth = 4

    def make_possible_moves(board):
        possible_moves = set()
        for row in range(len(board)):
            for col in range(len(board)):
                if board[row][col] != " ":
                    possible_moves = xoxo.update_possible_moves(board, possible_moves, (row, col))
        return possible_moves

    def test_win_row(self):
        board = [
            [" "," "," "," "," "," "],
            ["X","X","X","X","X"," "],
            [" "," "," "," "," "," "],
            [" "," "," "," "," "," "],
            [" "," "," "," "," "," "],
            [" "," "," "," "," "," "]
        ]
        last_move = (1, 2)
        self.assertTrue(xoxo.win_win(board, last_move))

        board = [
            [" "," "," "," "," "," "],
            [" ","X","X","X","X"," "],
            [" "," "," "," "," "," "],
            [" "," "," "," "," "," "],
            [" "," "," "," "," "," "],
            [" "," "," "," "," "," "]
        ]
        last_move = (1, 2)
        self.assertFalse(xoxo.win_win(board, last_move))

    def test_win_column(self):
        board = [
            [" "," "," "," "," "," "],
            [" "," "," ","X"," "," "],
            [" "," "," ","X"," "," "],
            [" "," "," ","X"," "," "],
            [" "," "," ","X"," "," "],
            [" "," "," ","X"," "," "]
        ]
        last_move = (1, 3)
        self.assertTrue(xoxo.win_win(board, last_move))

        board = [
            [" "," "," "," "," "," "],
            [" "," "," ","X"," "," "],
            [" "," "," ","X"," "," "],
            [" "," "," ","X"," "," "],
            [" "," "," "," "," "," "],
            [" "," "," ","X"," "," "]
        ]
        last_move = (3, 3)
        self.assertFalse(xoxo.win_win(board, last_move))

    def test_win_diagonal_left(self):
        board = [
            [" "," "," "," "," "," "],
            [" ","X"," ","X"," "," "],
            [" "," ","X","X"," "," "],
            [" "," "," ","X"," "," "],
            [" "," "," "," ","X"," "],
            [" "," "," "," "," ","X"]
        ]
        last_move = (1, 1)
        self.assertTrue(xoxo.win_win(board, last_move))
    
        board = [
            [" "," "," "," "," "," "],
            [" ","X"," ","X"," "," "],
            [" "," ","X","X"," "," "],
            [" "," "," "," "," "," "],
            [" "," "," "," ","X"," "],
            [" "," "," "," "," ","X"]
        ]
        last_move = (5, 5)
        self.assertFalse(xoxo.win_win(board, last_move))

    def test_win_diagonal_right(self):
        board = [
            [" "," "," "," "," ","X"],
            [" ","X"," ","X","X"," "],
            [" "," ","X","X"," "," "],
            [" "," ","X"," "," "," "],
            [" ","X"," "," ","X"," "],
            [" "," "," "," "," ","X"]
        ]
        last_move = (4, 1)
        self.assertTrue(xoxo.win_win(board, last_move))

        board = [
            [" "," "," "," "," ","X"],
            [" ","X"," ","X","X"," "],
            [" "," ","X","O"," "," "],
            [" "," ","X"," "," "," "],
            [" ","X"," "," ","X"," "],
            [" "," "," "," "," ","X"]
        ]
        last_move = (2, 3)
        self.assertFalse(xoxo.win_win(board, last_move))

    def test_evaluate_open_three_row_defense(self):
        board = [
            [" "," "," "," "," "," "," "," "],
            [" "," "," "," "," "," "," "," "],
            [" "," "," ","O","O","O"," "," "],
            [" "," "," "," "," "," "," "," "],
            [" "," "," ","X","X"," "," "," "],
            [" "," "," "," "," "," "," "," "],
            [" "," "," "," "," "," "," "," "],
            [" "," "," "," "," "," "," "," "]
        ]
        possible_moves = set()
        for row in range(len(board)):
            for col in range(len(board)):
                if board[row][col] != " ":
                    possible_moves = xoxo.update_possible_moves(board, possible_moves, (row, col))
        maxing = True
        last_move = (2, 3)
        move = xoxo.minimax(board, heuristics.heuristics, self.depth, maxing, last_move, possible_moves, alpha=float('-inf'), beta=float('inf'))
        self.assertIn((move[1]), [(2, 2),(2, 6)])

    def test_evaluate_open_three_row_offense(self):
        board = [
            [" "," "," "," "," "," "," "," "],
            [" "," "," "," "," "," "," "," "],
            [" "," "," ","O","O","O"," "," "],
            [" "," "," "," "," "," "," "," "],
            [" "," "," ","X","X","X"," "," "],
            [" "," "," "," "," "," "," "," "],
            [" "," "," "," "," "," "," "," "],
            [" "," "," "," "," "," "," "," "]
        ]
        possible_moves = set()
        for row in range(len(board)):
            for col in range(len(board)):
                if board[row][col] != " ":
                    possible_moves = xoxo.update_possible_moves(board, possible_moves, (row, col))
        maxing = True
        last_move = (2, 3)
        move = xoxo.minimax(board, heuristics.heuristics, self.depth, maxing, last_move, possible_moves, alpha=float('-inf'), beta=float('inf'))
        self.assertIn((move[1]), [(4, 2),(4, 6)])

    def test_evaluate_open_three_right_diag(self):
        board = [
            [" "," "," "," "," "," "," "," "],
            [" "," "," "," "," "," "," "," "],
            [" "," "," ","X"," ","O"," "," "],
            [" "," "," "," ","O"," "," "," "],
            [" "," "," ","O"," "," "," "," "],
            [" "," "," "," ","X"," "," "," "],
            [" "," "," "," "," "," "," "," "],
            [" "," "," "," "," "," "," "," "]
        ]
        possible_moves = set()
        for row in range(len(board)):
            for col in range(len(board)):
                if board[row][col] != " ":
                    possible_moves = xoxo.update_possible_moves(board, possible_moves, (row, col))
        maxing = True
        last_move = (3, 4)
        move = xoxo.minimax(board, heuristics.heuristics, self.depth, maxing, last_move, possible_moves, alpha=float('-inf'), beta=float('inf'))
        self.assertIn((move[1]), [(5, 2),(1, 6)])

    def test_evaluate_open_three_left_diag(self):
        board = [
            [" "," "," "," "," "," "," "," "],
            [" "," "," "," "," "," "," "," "],
            [" "," "," "," "," "," "," "," "],
            [" "," "," ","O"," "," "," "," "],
            [" "," "," "," ","O"," ","X"," "],
            [" "," "," ","X"," ","O"," "," "],
            [" "," "," "," "," "," "," "," "],
            [" "," "," "," "," "," "," "," "]
        ]
        possible_moves = set()
        for row in range(len(board)):
            for col in range(len(board)):
                if board[row][col] != " ":
                    possible_moves = xoxo.update_possible_moves(board, possible_moves, (row, col))
        maxing = True
        last_move = (4, 4)
        move = xoxo.minimax(board, heuristics.heuristics, self.depth, maxing, last_move, possible_moves, alpha=float('-inf'), beta=float('inf'))
        self.assertIn((move[1]), [(2, 2),(6, 6)])


    def test_is_it_draw(self):
        board = [
            ["X","O","X","O","X","O","X","O"],
            ["X","O","X","O","X","O","X","O"],
            ["O","X","O","X","O","X","O","X"],
            ["O","X","O","X","O","X","O","X"],
            ["X","O","X","O","X","O","X","O"],
            ["X","O","X","O","X","O","X","O"],
            ["O","X","O","X","O","X","O","X"],
            ["O","X","O","X","O","X","O","X"]
        ]

        possible_moves = set()
        for row in range(len(board)):
            for col in range(len(board)):
                if board[row][col] != " ":
                    possible_moves = xoxo.update_possible_moves(board, possible_moves, (row, col))
        maxing = True
        last_move = (5, 5)
        draw = xoxo.minimax(board, heuristics.heuristics, self.depth, maxing, last_move, possible_moves, alpha=float('-inf'), beta=float('inf'))
        self.assertEqual(draw[0], None)

    def test_left_diag_win_move(self):
        board = [
            [" "," "," "," "," "," "," "," "," "," "," "],
            [" "," "," "," "," ","X"," "," "," "," "," "],
            [" "," "," "," ","X","O"," "," ","X"," "," "],
            [" "," "," "," "," ","O"," ","O"," ","X"," "],
            [" "," "," ","X","O","O","O","X"," ","O"," "],
            [" "," "," "," ","X","O","O","O","X"," "," "],
            [" "," "," "," ","O","X","O","X"," "," "," "],
            [" "," "," ","X"," ","O","X"," "," "," "," "],
            [" "," "," "," ","X","X"," ","O"," "," "," "],
            [" "," "," "," ","O"," "," "," "," "," "," "],
            [" "," "," "," "," "," "," "," "," "," "," "]
        ]
        possible_moves = set()
        for row in range(len(board)):
            for col in range(len(board)):
                if board[row][col] != " ":
                    possible_moves = xoxo.update_possible_moves(board, possible_moves, (row, col))
        maxing = True
        last_move = (8, 7)
        move = xoxo.minimax(board, heuristics.heuristics, self.depth, maxing, last_move, possible_moves, alpha=float('-inf'), beta=float('inf'))
        self.assertEqual((move[1]), (3, 2))

    def test_left_diag_win_move1(self):
        board = [
            [" "," "," "," "," "," "," "," "," "," "," "],
            [" "," "," "," "," ","X"," "," "," "," "," "],
            [" "," "," "," ","X","O"," "," ","X"," "," "],
            [" "," ","O"," "," ","O"," ","O"," ","X"," "],
            [" "," "," ","X","O","O","O","X"," ","O"," "],
            [" "," "," "," ","X","O","O","O","X"," "," "],
            [" "," "," "," ","O","X","O","X"," "," "," "],
            [" "," "," ","X"," ","O","X"," "," "," "," "],
            [" "," "," ","X","X","X"," ","O"," "," "," "],
            [" "," "," "," ","O"," "," "," "," "," "," "],
            [" "," "," "," "," "," "," "," "," "," "," "]
        ]
        possible_moves = set()
        for row in range(len(board)):
            for col in range(len(board)):
                if board[row][col] != " ":
                    possible_moves = xoxo.update_possible_moves(board, possible_moves, (row, col))
        maxing = True
        last_move = (3, 2)
        move = xoxo.minimax(board, heuristics.heuristics, self.depth, maxing, last_move, possible_moves, alpha=float('-inf'), beta=float('inf'))
        self.assertEqual((move[1]), (8, 2))

    def test_left_diag_win_move2(self):
        board = [
            [" "," "," "," "," "," "," "," "," "," "," "],
            [" "," "," "," "," ","X"," "," "," "," "," "],
            [" "," "," "," ","X","O"," "," ","X"," "," "],
            [" "," ","O"," "," ","O"," ","O"," ","X"," "],
            [" "," "," ","X","O","O","O","X"," ","O"," "],
            [" "," "," "," ","X","O","O","O","X"," "," "],
            [" "," "," "," ","O","X","O","X"," "," "," "],
            [" "," "," ","X"," ","O","X"," "," "," "," "],
            [" ","O","X","X","X","X"," ","O"," "," "," "],
            [" "," "," "," ","O"," "," "," "," "," "," "],
            [" "," "," "," "," "," "," "," "," "," "," "]
        ]
        possible_moves = set()
        for row in range(len(board)):
            for col in range(len(board)):
                if board[row][col] != " ":
                    possible_moves = xoxo.update_possible_moves(board, possible_moves, (row, col))
        maxing = True
        last_move = (8, 1)
        move = xoxo.minimax(board, heuristics.heuristics, self.depth, maxing, last_move, possible_moves, alpha=float('-inf'), beta=float('inf'))
        self.assertEqual((move[1]), (8, 6))

    def test_right_diag_win_move(self): 
        board = [
            [" "," "," "," "," "," "," "," "," "," "," "],
            [" "," "," "," ","O"," "," "," "," "," "," "],
            [" "," "," "," ","X","X"," ","O"," "," "," "],
            [" "," "," ","X"," ","O","X"," "," "," "," "],
            [" "," "," "," ","O","X","O","X"," "," "," "],
            [" "," "," "," ","X","O","O","O","X"," "," "],
            [" "," "," ","X","O","O","O","X"," ","O"," "],
            [" "," "," "," "," ","O"," ","O"," ","X"," "],
            [" "," "," "," ","X","O"," "," ","X"," "," "],
            [" "," "," "," "," ","X"," "," "," "," "," "],
            [" "," "," "," "," "," "," "," "," "," "," "]
        ]
        possible_moves = set()
        for row in range(len(board)):
            for col in range(len(board)):
                if board[row][col] != " ":
                    possible_moves = xoxo.update_possible_moves(board, possible_moves, (row, col))
        maxing = True
        last_move = (2, 7)
        move = xoxo.minimax(board, heuristics.heuristics, self.depth, maxing, last_move, possible_moves, alpha=float('-inf'), beta=float('inf'))
        self.assertEqual((move[1]), (7, 2))

    def test_four_in_a_row_offense(self):
        board = [
            [" "," "," "," "," "," "," "," "],
            [" "," "," "," "," "," "," "," "],
            [" "," ","O","O","O","O"," "," "],
            [" "," "," "," "," "," "," "," "],
            [" "," ","X","X","X","X"," "," "],
            [" "," "," "," "," "," "," "," "],
            [" "," "," "," "," "," "," "," "],
            [" "," "," "," "," "," "," "," "]
        ]
        possible_moves = set()
        for row in range(len(board)):
            for col in range(len(board)):
                if board[row][col] != " ":
                    possible_moves = xoxo.update_possible_moves(board, possible_moves, (row, col))
        maxing = True
        last_move = (2, 3)
        move = xoxo.minimax(board, heuristics.heuristics, self.depth, maxing, last_move, possible_moves, alpha=float('-inf'), beta=float('inf'))
        self.assertIn((move[1]), [(4, 1),(4, 6)])

    def test_four_on_edge_defense(self):
        board = [
            [" "," "," "," "," "," "," "," "],
            [" "," "," "," "," "," "," "," "],
            ["O","O","O","O"," "," "," "," "],
            [" "," "," "," "," "," "," "," "],
            [" "," ","X","X","X"," "," "," "],
            [" "," "," "," "," "," "," "," "],
            [" "," "," "," "," "," "," "," "],
            [" "," "," "," "," "," "," "," "]
        ]
        possible_moves = set()
        for row in range(len(board)):
            for col in range(len(board)):
                if board[row][col] != " ":
                    possible_moves = xoxo.update_possible_moves(board, possible_moves, (row, col))
        maxing = True
        last_move = (2, 3)
        move = xoxo.minimax(board, heuristics.heuristics, self.depth, maxing, last_move, possible_moves, alpha=float('-inf'), beta=float('inf'))
        self.assertEqual((move[1]), (2, 4))

    def test_four_on_edge_offense(self):
        board = [
            [" "," "," "," "," "," "," "," "],
            [" "," "," "," "," "," "," "," "],
            ["X","X","X","X"," "," "," "," "],
            [" "," "," "," "," "," "," "," "],
            [" "," ","O","O","O","O"," "," "],
            [" "," "," "," "," "," "," "," "],
            [" "," "," "," "," "," "," "," "],
            [" "," "," "," "," "," "," "," "]
        ]
        possible_moves = set()
        for row in range(len(board)):
            for col in range(len(board)):
                if board[row][col] != " ":
                    possible_moves = xoxo.update_possible_moves(board, possible_moves, (row, col))
        maxing = True
        last_move = (4, 3)
        move = xoxo.minimax(board, heuristics.heuristics, self.depth, maxing, last_move, possible_moves, alpha=float('-inf'), beta=float('inf'))
        self.assertEqual((move[1]), (2, 4))
              

