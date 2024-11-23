# Kommentit ja testit vielä uupuu tässä vaiheessa :(
# Ja vielä itse pelin toiminnassa olisi säätämistä :((

def WinWin(board, last_move):
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

    while True:
        if y == 5:
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
        if x == 5:
            x = last_move[0]
            break
        if board[x][y] == board[x+1][y]:
            cd += 1
            x += 1
        else:
            x = last_move[0]
            break

    while True:
        if x == 5 or y == 5:
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
        if x == 0 or y == 5:
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
        if x == 5 or y == 0:
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

    best_score = float('-inf') if maxing else float('inf')
    best_move = None

    if WinWin(board, last_move):
        if maxing:
            best_score == 1111111111
            return best_score, last_move
        else:
            best_score == -1111111111
            return best_score, last_move
    
    if best_score == 1111111111 or best_score == -1111111111 :
        return best_score, last_move

    if depth == 0:
        return EvaluateBoard(board, heuristics), None

    
    
    for row in range(len(board)):
        for col in range(len(board[row])):
            if board[row][col] == ' ': 
                board[row][col] = "X" if maxing else "O"
                last_move = (row, col)
                score, move = Minimax(board, heuristics, depth - 1, not maxing, last_move)  
                
                board[row][col] = ' '
                
                if maxing:
                    if score > best_score:
                        best_score = score
                        best_move = (row, col)
                        #print(best_move, best_score)
                else:
                    if score < best_score:
                        best_score = score
                        best_move = (row, col)

    return best_score, best_move

def AiMakesMove(board, heuristics, last_move):
    best_score = float('-inf')
    best_move = None
    score, move = Minimax(board, heuristics, depth=2, maxing=True, last_move=last_move)
    if score < best_score:
        best_score = score
        best_move = move
    return best_move, best_score

def EvaluateBoard(board, heuristics):
    score = 0
    value = 0
    row_list, col_list, left_diag, right_diag = BoardToString(board)
   

    for key, value in heuristics.items():
        
        for row in row_list:
            if key in row:
                score += value
        
        if any(key in col for col in col_list):
            score += value

        for diag in left_diag:
            if key in diag:
                score += value
       
        if any(key in diag for diag in right_diag): 
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
     
    return col_list

def RowToString(board):
    row_list = []
    for row in board:
        row_string = ''.join(map(str, row))
        row_list.append(row_string)
    
    return row_list

def BoardToString(board):
    row_list = RowToString(board)
    col_list = ColToString(board)
    left_diag, right_diag = GetDiagonals(board)
    
    return row_list, col_list, left_diag, right_diag

def PlayTheGame(board, heuristics):
    for row in board:
        print(row)
    move = input("Move pls (row = 1-10, col = a-j):")
    board[int(move[0])-1][ord(move[1])-97] = "O"
    last_move = (int(move[0])-1, ord(move[1])-97)
    ai, value = AiMakesMove(board, heuristics, last_move)
    if ai is None:
        return 1
    if value == 1111111111:
        return 2
    if value == -1111111111:
        return 1
    
    board[int(ai[0])][int(ai[1])] = "X"
    return 0

def RollTheGame(board, heuristics):
    counter = 0
    while True:
        Hero = PlayTheGame(board, heuristics)
        #print(board)
        if Hero == 1: 
            print("Game over, O won the game!")
            break
        if Hero == 2:
            print("Game over, X won the game!")
            break
        else:
            counter += 1
            if counter == 10:
                break
    return "Hennesy"

if __name__ == "__main__":
    
    #board_size = 10
    #make_a_board = [[" " for i in range(board_size)] for j in range(board_size)]
    board = [
    [" ","X"," "," "," ","O"],
    [" ","X"," ","O","O"," "],
    [" ","X","O"," "," "," "],
    [" "," "," "," ","X"," "],
    ["O"," "," ","O","O","X"],
    ["X"," ","X"," "," "," "]
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
