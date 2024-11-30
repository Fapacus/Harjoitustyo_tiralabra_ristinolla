# kunnon testit vielä uupuu tässä vaiheessa :(
# virheellisten inputtien tarkistus puuttuu

def IsItDraw(board):
    """
    Checks if the board is full and in that case calls a draw.

    Args:
        board: The current board.

    Returns:
        True if the board is full, False otherwise.
    """
    for row in board:
        if " " in row:
            return False
    return True

def WinWin(board, last_move):
    
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
    if rr+rl >= 4 or cu+cd >= 4 or ldl+ldr >= 4 or rdl+rdr >= 4:
        check = True
    else:
        check = False

    return check

def Minimax(board, heuristics, depth, maxing, last_move):

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

    if WinWin(board, last_move):
        if not maxing:
            best_score = int(1111111111)
            return best_score, last_move
        else:
            best_score = int(-1111111111)
            return best_score, last_move
    if best_score == 1111111111 or best_score == -1111111111 :
        return best_score, last_move

    if IsItDraw(board):
        return None, last_move

    if depth == 0:
        score = EvaluateBoard(board, heuristics)
        return score, None

    
    
    for row in range(len(board)):
        for col in range(len(board[row])):
            if board[row][col] == ' ': 
                board[row][col] = "X" if maxing else "O"
                last_move = (row, col)
                score, move = Minimax(board, heuristics, depth - 1, not maxing, last_move)  
                
                board[row][col] = ' '
                
                if maxing:
                    if score == None:
                        board[row][col] = "X" if maxing else "O"
                        return score, last_move
                    if score > best_score:
                        best_score = score
                        best_move = (row, col)
    
                else:
                    if score < best_score:
                        best_score = score
                        best_move = (row, col)

    return best_score, best_move

def AiMakesMove(board, heuristics, last_move):
    """
    Calls the Minimax function to make a move.

    Args:
        board: The current board.
        heuristics: A dictionary with patterns and values.
        last_move: The last move made.

    Returns:
        Best move and its score unless draw has been detected.
    """
    best_score = float('-inf')
    best_move = None
    score, move = Minimax(board, heuristics, depth=2, maxing=True, last_move=last_move)

    if score == None:
        return last_move, score
    if score > best_score:
        best_score = score
        best_move = move
    print("Paras moovi ja pisteet sille: ",best_move, best_score)
    return best_move, best_score

def EvaluateBoard(board, heuristics):
    
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
    row_list, col_list, left_diag, right_diag = BoardToString(board)
   

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


def DiagonalsToStrings(board):
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


def ColToString(board):
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

def RowToString(board):
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

def BoardToString(board):
    """
    Calls the converting functions to convert the board into lists of strings.

    Args:
        board: The current board.

    Returns:
        Four lists of strings representing rows, columns, left diagonals and right diagonals.
    """
    row_list = RowToString(board)
    col_list = ColToString(board)
    left_diag, right_diag = DiagonalsToStrings(board)
    
    return row_list, col_list, left_diag, right_diag

def PlayTheGame(board, heuristics):
    """
    Asks the player to make a move and calls the AI to make a move. 
    Makes the final moves and passes the continution information of the game to the RollTheGame function.

    Args:
        board: The current board.
        heuristics: A dictionary with patterns and values.

    Returns:
        Returns 3 for a draw, 1 for a win by the human, or 2 for a win by the AI, and 0 if the game is not over. 
    """
    for row in board:
        print(row)
    print("")
    move = input("Move pls (row = 1-6, col = a-f) (example: 1a or 5b): ")
    board[int(move[0])-1][ord(move[1])-97] = "O"
    for row in board:
        print(row)
    print("")
    last_move = (int(move[0])-1, ord(move[1])-97)
    ai, value = AiMakesMove(board, heuristics, last_move)

    if ai is None:
        return 1
    
    board[int(ai[0])][int(ai[1])] = "X"
    
    if value == 1111111111:
        return 2
    if value == -1111111111:
        return 1
    if value == None:
        return 3
    
    
    return 0

def RollTheGame(board, heuristics):
    """
    Keeps the game going until either player wins or the board is full.

    Args:
        board: The current board.
        heuristics: A dictionary with patterns and values.

    Returns:
        Breaks the game roll and prints the result in case of a win or draw.
    """
    counter = 0
    while True:
        Hero = PlayTheGame(board, heuristics)
        if Hero == 1: 
            print("Game over, O won the game!")
            break
        if Hero == 2:
            print("Game over, X won the game!")
            break
        if Hero == 3:
            print("Game over, draw!")
            break
        else:
            continue
    for row in board:
        print(row)
    return "Hennesy"

if __name__ == "__main__":
    
    #board_size = 10
    #make_a_board = [[" " for i in range(board_size)] for j in range(board_size)]
    
    board = [
    [" "," "," "," "," ","O"],
    [" ","X"," ","O","O"," "],
    [" ","X","O"," "," "," "],
    [" ","X"," "," ","X"," "],
    ["O"," "," ","O","O","X"],
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

    RollTheGame(board, heuristics)
    #RollTheGame(board1, heuristics)
    #RollTheGame(board2, heuristics)
    #RollTheGame(board3, heuristics)
