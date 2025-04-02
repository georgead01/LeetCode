def isValidSudoku(board):
        
    rows = [set().copy() for _ in range(9)]
    cols = [set().copy() for _ in range(9)]
    sqrs = [set().copy() for _ in range(9)]

    for i in range(9):
        for j in range(9):

            if board[i][j] != '.':

                x = i//3
                y = j//3
                sq = x*3+y

                if board[i][j] in rows[i] or board[i][j] in cols[j] or board[i][j] in sqrs[sq]:
                    return False

                rows[i].add(board[i][j])
                cols[j].add(board[i][j])
                sqrs[sq].add(board[i][j])

    return True