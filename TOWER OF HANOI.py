from itertools import product


def create_state(positions):
    rods = [[], [], []]

    for disk in range(3, 0, -1):
        rod = positions[disk - 1]
        rods[rod].append(disk)

    return rods


def print_state(state, number):
    print("State", number)
    print("A:", state[0])
    print("B:", state[1])
    print("C:", state[2])
    print()


def generate_states():
    states = []

    for positions in product(range(3), repeat=3):
        state = create_state(positions)
        states.append(state)

    return states


states = generate_states()

print("TOTAL STATES =", len(states))
print()

for i, state in enumerate(states):
    print_state(state, i)

print("MAIN STATES")

initial_state = [[3, 2, 1], [], []]
goal_state = [[], [], [3, 2, 1]]

print("Initial State:")
print_state(initial_state, 0)

print("Goal State:")
print_state(goal_state, "Goal")

