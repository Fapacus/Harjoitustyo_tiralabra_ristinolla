import xoxo
import heuristics

def main():
    board_size = 20
    board = [[" " for i in range(board_size)] for j in range(board_size)]
    """
    board = [
            [" "," "," "," "," "," "," "," "," "," "," "," "],
            [" "," "," "," "," ","X"," "," "," "," "," "," "],
            [" "," "," "," ","X","O"," "," ","X"," "," "," "],
            [" "," "," "," "," ","O"," ","O"," ","X"," "," "],
            [" "," "," ","X","O","O","O","X"," ","O"," "," "],
            [" "," "," "," ","X","O","O","O","X"," "," "," "],
            [" "," "," "," ","O","X","O","X"," "," "," "," "],
            [" "," "," ","X"," ","O","X"," "," "," "," "," "],
            [" "," "," "," ","X","X"," "," "," "," "," "," "],
            [" "," "," "," ","O"," "," "," "," "," "," "," "],
            [" "," "," "," "," "," "," "," "," "," "," "," "],
            [" "," "," "," "," "," "," "," "," "," "," "," "]
        ]
    """

    print("")
    print("Welcome to XOXO!")
    print("Rules:\n"
          "Try to get 5 in a row as O-player and try to prevent X-player from getting 5 in a row.\n"
          "The board is 20x20. Rows are from 1 to 20, columns from a to t.\n"
          "Enter move in format: [row][col] or [col][row] (row = 1-20, col = a-t)\n"
          "Example: 1a or e15\n"
          )
    possible_moves = set()
    xoxo.roll_the_game(board, heuristics.heuristics, possible_moves)

main()
