def is_safe(board, row, col, n):
    # Check row on left
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check upper diagonal
    i, j = row, col
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1

    # Check lower diagonal
    i, j = row, col
    while j >= 0 and i < n:
        if board[i][j] == 1:
            return False
        i += 1
        j -= 1

    return True


def solve_nq_util(board, col, n):
    if col >= n:
        return True

    for row in range(n):
        if is_safe(board, row, col, n):
            board[row][col] = 1
            if solve_nq_util(board, col + 1, n):
                return True
            board[row][col] = 0

    return False


def solve_nq(n=8):
    board = [[0] * n for _ in range(n)]

    if solve_nq_util(board, 0, n):
        for row in board:
            print(row)
    else:
        print("No solution found")

solve_nq(8)
