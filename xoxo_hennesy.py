def Minimax(board, heuristics, depth, maxing):
    if depth == 0:
        return EvaluateBoard(board, heuristics), None

    best_score = float('-inf') if maxing else float('inf')
    best_move = None
    
    for row in range(len(board)):
        for col in range(len(board[row])):
            if board[row][col] == ' ': 
                
                board[row][col] = "O" if maxing else "X"
                score, move = Minimax(board, heuristics, depth - 1, not maxing)  
                
                board[row][col] = ' '
                
                if maxing:
                    if score > best_score:
                        best_score = score
                        best_move = (row, col)
                else:
                    if score < best_score:
                        best_score = score
                        best_move = (row, col)

    print("Best move:", best_move, "Best score:", best_score)
    return best_score, best_move

def AiMakesMove(board, heuristics):
    best_score = float('-inf')
    best_move = None
    score, move = Minimax(board, heuristics, depth=2, maxing=True)
    if score > best_score:
        best_score = score
        best_move = move
    print("BEST MOVE!!!:", best_move, "Best score:", best_score)
    return best_move

def EvaluateBoard(board, heuristics):
    score = 0
    value = 0
    row_list, col_list, left_diag, right_diag = BoardToString(board)
    print(left_diag)
    print("******")
    print(row_list)

    for key, value in heuristics.items():
        #print(row_list)
        #print(key)
        #print(heuristics.items())
        if any(key in row for row in row_list): #key in row_list:
            #print("HEPPPP!!!!!!!!!!!! ROW", key, "=", value)
            score += value
        if any(key in col for col in col_list): #key in col_list:
            #print("HEPPPP!!!!!!!!!!!! COL", key, "=", value)
            score += value
        if any(key in diag for diag in left_diag): #key in left_diag:
            print("HEPPPP!!!!!!!!!!!! LEFT", key, "=", value)
            score += value
        if any(key in diag for diag in right_diag): #key in right_diag:
            print("HEPPPP!!!!!!!!!!!! RIGHT", key, "=", value)
            score += value
    return score


def GetDiagonals(board):
    n = len(board) 
    
    left_diag = []  
    right_diag = []  
    
    for i in range(-n+1, n):
        left_diag_list = []  
        right_diag_list = []  
        for row in range(n):
            col1 = row + i  
            col2 = (n-1-row) - i  
            if 0 <= col1 < n:
                left_diag_list.append(board[row][col1])
            if 0 <= col2 < n:
                right_diag_list.append(board[row][col2])
        
        if len(left_diag_list) >= 3:
            left_diag_string = ''.join(map(str, left_diag_list))
            left_diag.append(left_diag_string)
        if len(right_diag_list) >= 3:
            right_diag_string = ''.join(map(str, right_diag_list))
            right_diag.append(right_diag_string)
    
    return left_diag, right_diag


def ColToString(board):
    col_list = []
    for col in zip(*board):
        col_string = ''.join(map(str, col))
        col_list.append(col_string)
    
    #print(col_list)  
    return col_list

def RowToString(board):
    row_list = []
    for row in board:
        row_string = ''.join(map(str, row))
        row_list.append(row_string)
    
    #print(row_list)  
    return row_list

def BoardToString(board):
    row_list = RowToString(board)
    col_list = ColToString(board)
    left_diag, right_diag = GetDiagonals(board)
    
    return row_list, col_list, left_diag, right_diag

def PlayTheGame(board, heuristics):
    for row in board:
        print(row)
    #print(board)
    move = input("Move pls (row = 1-10, col = a-j):")
    board[int(move[0])-1][ord(move[1])-97] = "X"
    for row in board:
        print(row)
    BoardToString(board)
    print("******")
    aiaiai = AiMakesMove(board, heuristics)
    print("aiaiai:", aiaiai)
    print(aiaiai[0], aiaiai[1])
    print(board)
    print("boardi on:", board[5][3])
    board[aiaiai[0]][aiaiai[1]] = "O"
    print("boardi on nyt:", board[5][3])
    print(board[aiaiai[0]][aiaiai[1]])
    print(board)
    for row in board:
        print(row)
    return "Hennesy"

def RollTheGame(board, heuristics):
    counter = 0
    while True:
        PlayTheGame(board, heuristics)
        counter += 1
        if counter == 10:
            break
    return "Hennesy"

if __name__ == "__main__":
    
    board_size = 10
    make_a_board = [["_" for i in range(board_size)] for j in range(board_size)]
    board = [
    [" ","X"," "," "," ","O"],
    [" ","X","X","O","O"," "],
    [" ","X","O","X"," "," "],
    [" "," "," "," "," "," "],
    ["O","O"," ","O","O","X"],
    ["X"," ","X"," "," "," "]
    ]

    
    heuristics = {
        "XXXXX": 100000000,
        "OOOOO": -100000000,
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
        " XX ": 4,
        " OO ": -4,
        
        " X ": 1,
        " O ": -1  
    }

    #print(PlayTheGame(make_a_board))
    RollTheGame(board, heuristics)
