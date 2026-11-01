def misplaced_tiles(board, goal):
    count = 0
    for i in range(9):
        if board[i] != 0 and board[i] != goal[i]:
            count += 1
    return count

def get_moves(board):
    moves = []
    pos = board.index(0)
    row = pos // 3
    col = pos % 3

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for dr, dc in directions:
        new_row = row + dr
        new_col = col + dc

        if 0 <= new_row < 3 and 0 <= new_col < 3:
            new_pos = new_row * 3 + new_col
            new_board = list(board)
            new_board[pos], new_board[new_pos] = new_board[new_pos], new_board[pos]
            moves.append(new_board)

    return moves

def a_star(start, goal):
    open_list = [(misplaced_tiles(start, goal), 0, start, [start])]
    visited = []

    while open_list:
        open_list.sort()
        f, cost, board, path = open_list.pop(0)

        if board == goal:
            return path

        if board in visited:
            continue

        visited.append(board)

        for new_board in get_moves(board):
            if new_board not in visited:
                new_cost = cost + 1
                h = misplaced_tiles(new_board, goal)
                open_list.append((new_cost + h, new_cost, new_board, path + [new_board]))

    return None

start = [1, 2, 3, 4, 0, 6, 7, 5, 8]
goal = [1, 2, 3, 4, 5, 6, 7, 8, 0]

path = a_star(start, goal)

if path:
    for board in path:
        for i in range(0, 9, 3):
            print(board[i:i + 3])
        print()

    print("Total moves:", len(path) - 1)
else:
    print("No solution")


