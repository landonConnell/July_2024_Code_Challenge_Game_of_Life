def get_num_neighbors(board, row, column):
    num_neighbors = 0

    # board dimensions
    width = len(board[0])
    height = len(board)

    # indices of cells surrounding (row, column)
    up = row - 1
    down = row + 1
    left = column - 1
    right = column + 1
    
    # add neighbor immediately above (row, column)
    if up >= 0: num_neighbors += board[up][column]

    # add neighbor immediately below (row, column)
    if down < height: num_neighbors += board[down][column]

    # find all neighbors to the left of (row, column)
    if left >= 0:
        num_neighbors += board[row][left] # left neighbor
        if up >= 0: num_neighbors += board[up][left] # top-left neighbor
        if down < height: num_neighbors += board[down][left] # bottom-left neighbor
    
    # find all neighbors to the right of (row, column)
    if right < width:
        num_neighbors += board[row][right] # right neighbor
        if up >= 0: num_neighbors += board[up][right] # top-right neighbor
        if down < height: num_neighbors += board[down][right] # bottom-right neighbor

    return num_neighbors

def get_next_state(board):
    
    # a two-dimensional array, where each sub-array represents a row, and
    # each of the elements in the sub-array represents a column to switch
    rows_to_switch = []

    for row in range(len(board)):
        columns_to_switch = []
        for column in range(len(board[row])):
            num_neighbors = get_num_neighbors(board, row, column)
            if board[row][column] == 1 and (num_neighbors < 2 or num_neighbors > 3): # rules 1 and 3
                columns_to_switch.append(column)
            elif board[row][column] == 0 and num_neighbors == 3: # rule 4
                columns_to_switch.append(column)
            # else - rule 2
        rows_to_switch.append(columns_to_switch)

    row = 0
    for columns_to_switch in rows_to_switch:
        for column in columns_to_switch:
            board[row][column] = 0 if board[row][column] == 1 else 1
        row += 1

    return board
