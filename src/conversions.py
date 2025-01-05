def diagonals_to_strings(board):
    """
    Converts the board into two lists of strings representing diagonals from left and right.

    Args:
        board: The current board.

    Returns:
        Two lists of strings representing left and right diagonals.
    """
    limit = len(board) - 1
    n = len(board)

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

    for start_col in range(n-1, -1, -1):
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
