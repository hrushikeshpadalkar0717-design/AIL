def is_safe(board, row, col):
    for i in range(row):
        if board[i] == col or abs(board[i] - col) == abs(i - row):
            return False
    return True


def print_board(board, message):
    print("\n" + message)
    for r in range(8):
        print(" ".join("Q" if board[r] == c else "." for c in range(8)))


def solve(board, row):
    if row == 8:
        print_board(board, "GOAL STATE")
        return True

    for col in range(8):
        if is_safe(board, row, col):
            board[row] = col
            print_board(board, f"Queen placed at Row {row + 1}, Column {col + 1}")

            if solve(board, row + 1):
                return True

            board[row] = -1
            print(f"Backtracking occurred: Queen removed from Row {row + 1}")

    return False


board = [-1] * 8
print_board(board, "INITIAL STATE")

solve(board, 0)
