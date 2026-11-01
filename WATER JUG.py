def dfs(capacity1, capacity2, goal):
    start = (0, 0)
    stack = [(start, [start])]
    visited = set()

    while stack:
        current, path = stack.pop()
        jug1, jug2 = current

        if current in visited:
            continue

        visited.add(current)

        print("\nCurrent Percept:")
        print("Jug 1:", jug1, "litres")
        print("Jug 2:", jug2, "litres")
        print("Current State:", current)

        if jug1 == goal or jug2 == goal:
            print("\nGoal Reached!")
            return path, visited

        states = [
            (capacity1, jug2),                  # Fill Jug 1
            (jug1, capacity2),                  # Fill Jug 2
            (0, jug2),                          # Empty Jug 1
            (jug1, 0),                          # Empty Jug 2
            (jug1 - min(jug1, capacity2-jug2),
             jug2 + min(jug1, capacity2-jug2)), # Pour Jug 1 to Jug 2
            (jug1 + min(jug2, capacity1-jug1),
             jug2 - min(jug2, capacity1-jug1))  # Pour Jug 2 to Jug 1
        ]

        for state in states:
            if state not in visited and state != current:
                stack.append((state, path + [state]))

    return None, visited


capacity1 = 4
capacity2 = 3
goal = 2

path, visited = dfs(capacity1, capacity2, goal)

print("\n========== ALL VISITED STATES ==========")
for state in visited:
    print("Jug 1:", state[0], "litres | Jug 2:", state[1], "litres")

print("\n========== FINAL SOLUTION PATH ==========")
if path:
    for i, state in enumerate(path, 1):
        print("Step", i,
              "| Jug 1:", state[0], "litres",
              "| Jug 2:", state[1], "litres")
else:
    print("No solution found")

