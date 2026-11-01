distance = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

n = 4
k = 3

def cost(route):
    total = 0
    for i in range(n - 1):
        total += distance[route[i]][route[i + 1]]
    total += distance[route[n - 1]][route[0]]
    return total

def generate_neighbors(route):
    neighbors = []
    for i in range(1, n):
        for j in range(i + 1, n):
            new_route = route[:]
            new_route[i], new_route[j] = new_route[j], new_route[i]
            neighbors.append(new_route)
    return neighbors

def print_states(states):
    for i, route in enumerate(states):
        print("State", i + 1, ":", end=" ")
        print(" ".join(str(city + 1) for city in route),
              "-> 1   Cost =", cost(route))

states = [
    [0, 1, 2, 3],
    [0, 1, 3, 2],
    [0, 2, 1, 3]
]

print("Initial States:")
print_states(states)

for iteration in range(1, 6):
    all_neighbors = []

    for route in states:
        all_neighbors.extend(generate_neighbors(route))

    all_neighbors.sort(key=cost)
    states = all_neighbors[:k]

    print("\nIteration", iteration, ":")
    print_states(states)

best = min(states, key=cost)

print("\nBest Solution:")
print("Route:", " -> ".join(str(city + 1) for city in best), "-> 1")
print("Minimum Cost:", cost(best))

