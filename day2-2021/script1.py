with open("data") as file:
    depth = 0
    horizontal = 0
    for line in file:
        instruction = line.split(" ")
        direction = instruction[0]
        amount = int(instruction[1])
        if direction == "down":
            depth += amount
        if direction == "up":
            depth -= amount
        if direction == "forward":
            horizontal += amount

    print(depth * horizontal)

