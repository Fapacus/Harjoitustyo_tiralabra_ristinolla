import time


def update_possible_moves(board, possible_moves, last_move):
    """
    Updates the possible moves based on the last move.

    Args:
        board: The current board.
        possible_moves: The possible moves.
        last_move: The last move made.

    Returns:
        The updated possible moves.
    """
    moves_set = set(possible_moves)
    x = last_move[0]
    y = last_move[1]

    limit = len(board)-1

    for i in range(x-3, x+3):
        if i < 0:
            continue
        if i > limit:
            break
        for j in range(y-3, y+3):
            if j < 0:
                continue
            if j > limit:
                break
            if board[i][j] == " ":
                moves_set.add((i,j))
            
    moves_set.discard(last_move)
    
    return moves_set


def win_win(board, last_move, depth):
    """
    Checks if the game has been won after a move.

    Args:
        board: The current board.
        last_move: The last move made.

    Returns:
        True if the game has been won, False otherwise.
    """
    rr = 0
    rl = 0
    cu = 0
    cd = 0
    ldr = 0
    ldl = 0
    rdr = 0
    rdl = 0

    x = last_move[0]
    y = last_move[1]

    limit = len(board)-1

    while True:
        if y == limit:
            y = last_move[1]
            break
        if board[x][y] == board[x][y+1]:
            rr += 1
            y += 1
        else:
            y = last_move[1]
            break

    while True:
        if y == 0:
            y = last_move[1]
            break
        if board[x][y] == board[x][y-1]:
            rl += 1
            y -= 1
        else:
            y = last_move[1]
            break

    if rr+rl >= 4:
        return True

    while True:
        if x == 0:
            x = last_move[0]
            break
        if board[x][y] == board[x-1][y]:
            cu += 1
            x -= 1
        else:
            x = last_move[0]
            break

    while True:
        if x == limit:
            x = last_move[0]
            break
        if board[x][y] == board[x+1][y]:
            cd += 1
            x += 1
        else:
            x = last_move[0]
            break
    if cu+cd >= 4:
        return True

    while True:
        if x == limit or y == limit:
            x = last_move[0]
            y = last_move[1]
            break
        if board[x][y] == board[x+1][y+1]:
            ldr += 1
            x += 1
            y += 1
        else:
            x = last_move[0]
            y = last_move[1]
            break

    while True:
        if x == 0 or y == 0:
            x = last_move[0]
            y = last_move[1]
            break
        if board[x][y] == board[x-1][y-1]:
            ldl += 1
            x -= 1
            y -= 1
        else:
            x = last_move[0]
            y = last_move[1]
            break
    
    if ldr+ldl >= 4:
        return True

    while True:
        if x == 0 or y == limit:
            x = last_move[0]
            y = last_move[1]
            break
        if board[x][y] == board[x-1][y+1]:
            rdr += 1
            x -= 1
            y += 1
        else:
            x = last_move[0]
            y = last_move[1]
            break

    while True:
        if x == limit or y == 0:
            x = last_move[0]
            y = last_move[1]
            break
        if board[x][y] == board[x+1][y-1]:
            rdl += 1
            x += 1
            y -= 1
        else:
            x = last_move[0]
            y = last_move[1]
            break

    if rdl+rdr >= 4:
        return True
    
    return False

def minimax(board, heuristics, depth, maxing, last_move, possible_moves, alpha=float('-inf'), beta=float('inf')):

    """
    Checks if the game has been won or drawn, 
    and then makes a move based on the evaluation of the board.

    Args:
        board: The current board.
        heuristics: A dictionary with patterns and values.
        depth: The currentdepth of the search.
        maxing: Whether the AI is maximizing or minimizing.
        last_move: The last move made.

    Returns:
        Best move and its score.
    """
    best_score = float('-inf') if maxing else float('inf')
    best_move = None

    if win_win(board, last_move, depth):
        if not maxing:
            best_score = int(1111111111)*(depth**depth)
            return best_score, last_move
        best_score = int(-1111111111)*(depth**depth)
        return best_score, last_move
    

    if len(possible_moves) == 0:
        return None, last_move

    if depth == 0:
        score = evaluate_board(board, heuristics)
        return score, None
    
    for move in possible_moves:
        row, col = move
        if board[row][col] == ' ':
            board[row][col] = "X" if maxing else "O"
            last_move = (row, col)

            new_possible_moves = update_possible_moves(board, possible_moves, last_move)

            score, _ = minimax(board, heuristics, depth - 1, not maxing, last_move, new_possible_moves, alpha, beta)           
            board[row][col] = ' '
            if maxing:
                if score is None:
                    board[row][col] = "X" if maxing else "O"
                    return score, last_move
                if score > best_score:
                    best_score = score
                    best_move = (row, col)
                alpha = max(alpha, score)
            else:
                if score < best_score:
                    best_score = score
                    best_move = (row, col)
                beta = min(beta, score)

            if beta <= alpha:
                break

    return best_score, best_move

def ai_makes_move(board, heuristics, last_move, possible_moves, depth):
    start_time = time.time()
    """
    Calls the minimax function to make a move.

    Args:
        board: The current board.
        heuristics: A dictionary with patterns and values.
        last_move: The last move made.

    Returns:
        Best move and its score unless draw has been detected.
    """
    best_score = float('-inf')
    best_move = None
    score, move = minimax(board, heuristics, depth, maxing=True, last_move=last_move, possible_moves=possible_moves, alpha=float('-inf'), beta=float('inf'))

    if score is None:
        return last_move, score
    if score > best_score:
        best_score = score
        best_move = move
    end_time = time.time()
    print("Aika: ", end_time - start_time)
    return best_move, best_score

def evaluate_board(board, heuristics):
    """
    Evaluates the current board based on the given heuristics.

    Args:
        board: The current board.
        heuristics: heuristics: A dictionary with patterns and values.

    Returns:
        The score of the board.
    """
    score = 0
    value = 0
    row_list, col_list, left_diag, right_diag = board_to_string(board)

    for key, value in heuristics.items():
        for row in row_list:
            if key in row:
                score += value
        for col in col_list:
            if key in col:
                score += value

        for diag in left_diag:
            if key in diag:
                score += value
        for diag in right_diag:
            if key in diag:
                score += value

    return score


def diagonals_to_strings(board):
    """
    Converts the board into two lists of strings representing diagonals from left and right.

    Args:
        board: The current board.

    Returns:
        Two lists of strings representing left and right diagonals.
    """
    limit = len(board) - 1
    n = limit - 4

    left_diag = []

    for start_row in range(n):
        diag = []
        row, col = start_row, 0
        while row < limit and col < limit:
            diag.append(board[row][col])
            row += 1
            col += 1
        left_diag.append(''.join(diag))

    for start_col in range(1, n):
        diag = []
        row, col = 0, start_col
        while row < limit and col < limit:
            diag.append(board[row][col])
            row += 1
            col += 1
        left_diag.append(''.join(diag))

    right_diag = []

    for start_row in range(n):
        diag = []
        row, col = start_row, limit
        while row < limit and col >= 0:
            diag.append(board[row][col])
            row += 1
            col -= 1
        right_diag.append(''.join(diag))

    for start_col in range(n - 2, -1, -1):
        diag = []
        row, col = 0, start_col
        while row < limit and col >= 0:
            diag.append(board[row][col])
            row += 1
            col -= 1
        right_diag.append(''.join(diag))

    return left_diag, right_diag


def col_to_string(board):
    """
    Converts the board into a list of strings representing columns.

    Args:
        board: The current board.

    Returns:
        A list of strings representing columns.
    """
    col_list = []
    n = len(board)

    for i in range(n):
        col = []
        for row in board:
            col.append(row[i])
        col_string = ''.join(col)
        col_list.append(col_string)

    return col_list

def row_to_string(board):
    """
    Converts the board into a list of strings representing rows.

    Args:
        board: The current board.

    Returns:
        A list of strings representing rows.
    """
    row_list = []
    for row in board:
        row_string = ''.join(row)
        row_list.append(row_string)
    return row_list

def board_to_string(board):
    """
    Calls the converting functions to convert the board into lists of strings.

    Args:
        board: The current board.

    Returns:
        Four lists of strings representing rows, columns, left diagonals and right diagonals.
    """
    row_list = row_to_string(board)
    col_list = col_to_string(board)
    left_diag, right_diag = diagonals_to_strings(board)
    return row_list, col_list, left_diag, right_diag

def play_the_game(board, heuristics, possible_moves):
    """
    Asks the player to make a move and calls the AI to make a move. 
    Makes the final moves and passes the continution information 
    of the game to the roll_the_game function.

    Args:
        board: The current board.
        heuristics: A dictionary with patterns and values.

    Returns:
        Returns 3 for a draw, 1 for a win by the human, 
        or 2 for a win by the AI, and 0 if the game is not over. 
    """
    draw_board(board)

    while True:
        move = input("Move pls, row first then col (row = 1-6, col = a-f) (example: 1a or 5b): ")
        if move[0] not in "123456" or move[1] not in "abcdef" or board[int(move[0])-1][ord(move[1])-97] != " ":
            print("Invalid move, try again.")
            continue
        break
    board[int(move[0])-1][ord(move[1])-97] = "O"
    
    possible_moves = update_possible_moves(board, possible_moves, (int(move[0])-1, ord(move[1])-97))
    draw_board(board)
    last_move = (int(move[0])-1, ord(move[1])-97)
    depth = 5
    ai, value = ai_makes_move(board, heuristics, last_move, possible_moves, depth)

    if ai is None:
        return 1
    if value == 1111111111*((depth-1)**(depth-1)):
        board[int(ai[0])][int(ai[1])] = "X"
        return 2
    if value == -1111111111*(depth**depth):
        return 1
    if value is None:
        return 3
    board[int(ai[0])][int(ai[1])] = "X"
    return 0

def roll_the_game(board, heuristics, possible_moves):
    """
    Keeps the game going until either player wins or the board is full.

    Args:
        board: The current board.
        heuristics: A dictionary with patterns and values.

    Returns:
        Breaks the game roll and prints the result in case of a win or draw.
    """
    while True:
        hero = play_the_game(board, heuristics, possible_moves)
        if hero == 1:
            print("Game over, O won the game!")
            break
        if hero == 2:
            print("Game over, X won the game!")
            break
        if hero == 3:
            print("Game over, draw!")
            break
        continue
    draw_board(board)
    return "Hennesy"

def draw_board(board):
    """
    Draws the board in the terminal.

    Args:
        board: The current board.

    Returns:
        None
    """
    print("   " + " ".join("a b c d e f".split()))
    for i, row in enumerate(board, 1):
         print(f"{i} " + "|" + "|".join(row) + "|")
    print("")

if __name__ == "__main__":
    #board_size = 10
    #make_a_board = [[" " for i in range(board_size)] for j in range(board_size)]
    board0 = [
    [" "," "," "," "," "," "],
    [" "," "," "," "," "," "],
    [" ","X","X","X"," "," "],
    [" "," "," "," "," "," "],
    [" ","O","O","O"," "," "],
    [" "," "," "," "," "," "]
    ]
    
    board = [
    [" "," "," "," "," ","O"],
    [" ","X"," ","O","O"," "],
    [" ","X","O","O"," "," "],
    [" ","X"," ","O","X"," "],
    ["O"," ","O","O","O","X"],
    ["X","X","X"," "," "," "]
    ]

    board1 = [
    [" ","O","O","X","X","X"],
    ["X","X","X","O","O","O"],
    ["O","O","O","X","X","X"],
    ["X","X","X","O","O","O"],
    ["O","O","O","X","X","X"],
    ["X","X","X","O","O","O"],
    ]

    board2 = [
    [" ","O","O","X","X","X"],
    [" ","X","X","O","O","O"],
    ["O","O","O","X","X","X"],
    ["X","X","X","O","O","O"],
    ["O","O","O","X","X","X"],
    ["X","X","X","O","O","O"],
    ]

    board3 = [
    [" ","X"," "," ","O","O"],
    ["O"," ","X","O","O","X"],
    [" "," ","O"," "," "," "],
    [" "," "," ","X","X"," "],
    ["O"," ","X","O","O","X"],
    ["X","X","X"," ","O"," "]
    ]

    heuristics = {
        " XXXX ": 50000000,
        " OOOO ": -50000000,
        "XXXX ": 1000000,
        " XXXX": 1000000,
        "OOOO ": -1000000,
        " OOOO": -1000000,
        "XX XX": 1000000,
        "OO OO": -1000000,
        "X XXX": 1000000,
        "O OOO": -1000000,
        "XXX X": 1000000,
        "OOO O": -1000000,
        "  XXX  ": 50000,
        "  OOO  ": -50000,
        " XXX ": 20000,
        " OOO ": -20000,
        " XX ": 40,
        " OO ": -40,
        " X ": 1,
        " O ": -1  
    }

    possible_moves = []
    def make_possible_moves(board):
        for row in range(len(board)):
            for col in range(len(board)):
                if board[row][col] != " ":
                    possible_move = update_possible_moves(board, possible_moves, (row, col))
        return possible_move

    roll_the_game(board0, heuristics, make_possible_moves(board0))
    roll_the_game(board, heuristics, make_possible_moves(board))
    roll_the_game(board1, heuristics, make_possible_moves(board1))
    roll_the_game(board2, heuristics, make_possible_moves(board2))
    #roll_the_game(board3, heuristics, make_possible_moves(board3))