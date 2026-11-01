def vacuum_agent(location, status):
    if status == "Dirty":
        return "Suck"
    elif location == "A":
        return "Right"
    else:
        return "Left"


environment = {
    "A": "Dirty",
    "B": "Dirty"
}

location = "A"
performance = 0

while "Dirty" in environment.values():
    status = environment[location]
    action = vacuum_agent(location, status)

    print("Location:", location, "| Status:", status, "| Action:", action)

    if action == "Suck":
        environment[location] = "Clean"
        performance += 1
    elif action == "Right":
        location = "B"
    elif action == "Left":
        location = "A"

print("Final Environment:", environment)
print("Performance Score (suck):", performance)

