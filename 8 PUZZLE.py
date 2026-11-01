from collections import deque

start = (1, 2, 3,
         0, 4, 6,
         7, 5, 8)

goal = (1, 2, 3,
        4, 5, 6,
        7, 8, 0)

def moves(state):
    result = []
    pos = state.index(0)
    r, c = divmod(pos, 3)

    for dr, dc, name in [
        (-1, 0, "Up"),
        (1, 0, "Down"),
        (0, -1, "Left"),
        (0, 1, "Right")
    ]:
        nr, nc = r + dr, c + dc

        if 0 <= nr < 3 and 0 <= nc < 3:
            new = list(state)
            new[pos], new[nr * 3 + nc] = new[nr * 3 + nc], new[pos]
            result.append((tuple(new), name))

    return result

def bfs():
    queue = deque([(start, [])])
    visited = {start}

    while queue:
        state, path = queue.popleft()

        if state == goal:
            return path

        for new_state, move in moves(state):
            if new_state not in visited:
                visited.add(new_state)
                queue.append((new_state, path + [(new_state, move)]))

    return None

def print_state(state):
    print(state[:3])
    print(state[3:6])
    print(state[6:])

solution = bfs()

print("Initial State:")
print_state(start)

print("\nSolution Steps:")
if solution is not None:
    for i, (state, move) in enumerate(solution):
        print("\nStep", i + 1, "- Move", move)
        print_state(state)

    print("\nGoal State:")
    print_state(goal)
    print("\nTotal Steps:", len(solution))
else:
    print("No solution found")
