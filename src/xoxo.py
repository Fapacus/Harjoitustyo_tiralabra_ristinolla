import time
import conversions


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

    for i in range(x-2, x+3):
        if i < 0:
            continue
        if i > limit:
            break
        for j in range(y-2, y+3):
            if j < 0:
                continue
            if j > limit:
                break
            if board[i][j] == " ":
                moves_set.add((i,j))
    
    moves_set.discard(last_move)
    

    return moves_set
   
def win_win(board, last_move):
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

    
    if win_win(board, last_move):
        if not maxing:
            best_score = int(1111111111)*(depth**depth)
            return best_score, last_move
        best_score = int(-1111111111)*(depth**depth)
        return best_score, last_move
    

    if len(possible_moves) == 0:
        return None, last_move

    if depth == 0:
        score = evaluate_board(board, heuristics, maxing)
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
    print("Time: ", end_time - start_time)
    print(f"AI's move: {int(best_move[0]+1)}{chr(best_move[1]+97)}")
    return best_move, best_score

def evaluate_board(board, heuristics, maxing):
    """
    Evaluates the current board based on the given heuristics.

    Args:
        board: The current board.
        heuristics: heuristics: A dictionary with patterns and values.
        maxing: Whether the AI is maximizing or minimizing.

    Returns:
        The score of the board.
    """
    score = 0
    value = 0
    row_list, col_list, left_diag, right_diag = board_to_string(board)
    print(maxing)
    if maxing:
        for key, value in heuristics.items():
            for row in row_list:
                if key in row:
                    if value > 0:
                        score += value*2
                    else:
                        score += value
            for col in col_list:
                if key in col:
                    if value > 0:
                        score += value*2
                    else:
                        score += value

            for diag in left_diag:
                if key in diag:
                    if value > 0:
                        score += value*2
                    else:
                        score += value
            for diag in right_diag:
                if key in diag:
                    if value > 0:
                        score += value*2
                    else:
                        score += value
    
    else:
        for key, value in heuristics.items():
            for row in row_list:
                if key in row:
                    if value < 0:
                        score += value
                    else:
                        score += value
            for col in col_list:
                if key in col:
                    if value < 0:
                        score += value
                    else:
                        score += value

            for diag in left_diag:
                if key in diag:
                    if value < 0:
                        score += value
                    else:
                        score += value
    return score

def board_to_string(board):
    """
    Calls the converting functions to convert the board into lists of strings.

    Args:
        board: The current board.

    Returns:
        Four lists of strings representing rows, columns, left diagonals and right diagonals.
    """
    row_list = conversions.row_to_string(board)
    col_list = conversions.col_to_string(board)
    left_diag, right_diag = conversions.diagonals_to_strings(board)
    return row_list, col_list, left_diag, right_diag

def play_the_game(board, heuristics, possible_moves):
    """
    Asks the player to make a move and calls the AI to make a move. 
    Makes the final moves and passes the continuation information 
    of the game to the roll_the_game function.

    Args:
        board: The current board.
        heuristics: A dictionary with patterns and values.
        possible_moves: A list of possible moves.

    Returns:
        Returns 3 for a draw, 1 for a win by the human, 
        or 2 for a win by the AI, and 0 and "ai" as a ai move if the game is not over. 
    """
    draw_board(board)

    while True:
        move = input("Your move: ")
        if len(move) == 2:
            if move[0] in "123456789" and move[1] in "abcdefghijklnmopqrst":
                row = int(move[0])-1
                col = ord(move[1])-97
                if board[row][col] != " ":
                    print("Invalid move, try again.")
                    continue
                break
            if move[1] in "123456789" and move[0] in "abcdefghijklnmopqrst":
                col = ord(move[0])-97
                row = int(move[1])-1
                if board[row][col] != " ":
                    print("Invalid move, try again.")
                    continue
                break
            else:
                print("Invalid move, try again.")
                continue
        if len(move) == 3:
            if move[0] == "1" and move[1] in "0123456789" and move[2] in "abcdefghijklnmopqrst":
                row = int(move[:2])-1
                col = ord(move[2])-97
                if board[row][col] != " ":
                    print("Invalid move, try again.")
                    continue
                break
            if move[0] == "2" and move[1] == "0" and move[2] in "abcdefghijklnmopqrst":
                row = int(move[:2])-1
                col = ord(move[2])-97
                if board[row][col] != " ":
                    print("Invalid move, try again.")
                    continue
                break
            if move[0] in "abcdefghijklnmopqrst" and move[1] == "1" and move[2] in "0123456789":
                col = ord(move[0])-97
                row = int(move[1:])-1
                if board[row][col] != " ":
                    print("Invalid move, try again.")
                    continue
                break
            if move[0] in "abcdefghijklnmopqrst" and move[1] == "2" and move[2] == "0":
                col = ord(move[0])-97
                row = int(move[1:])-1
                if board[row][col] != " ":
                    print("Invalid move, try again.")
                    continue
                break
            else:
                print("Invalid move, try again.")
                continue
        else:
            print("Invalid move, try again.")
            continue
    board[row][col] = "O"

    last_move = (row, col)
    possible_moves = update_possible_moves(board, possible_moves, last_move)
    draw_board(board)
    
    depth = 4
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
    return 0, ai

def roll_the_game(board, heuristics, possible_moves):
    """
    Keeps the game going until either player wins or the board is full.

    Args:
        board: The current board.
        heuristics: A dictionary with patterns and values.
        possible_moves: A list of possible moves.

    Returns:
        Breaks the game roll and prints the result in case of a win or draw.
    """
    while True:
        hero, ai = play_the_game(board, heuristics, possible_moves)
        if hero == 1:
            print("Game over, YOU won the game!")
            break
        if hero == 2:
            print("Game over, AI won the game!")
            break
        if hero == 3:
            print("Game over, draw!")
            break
        possible_moves = update_possible_moves(board, possible_moves, ai)
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
    print("    " + " ".join("a b c d e f g h i j k l m n o p q r s t".split()))
    for i, row in enumerate(board, 1):
        if i < 10:
            print(f" {i}:" + "|" + "|".join(row) + "|")
        else:
            print(f"{i}:" + "|" + "|".join(row) + "|")
    print("")
