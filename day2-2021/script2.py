with open("data") as file:
    depth = 0
    horizontal = 0
    aim = 0
    for line in file:
        instruction = line.split(" ")
        direction = instruction[0]
        amount = int(instruction[1].split("\n")[0])
        if direction == "down":
            aim += amount
        if direction == "up":
            aim -= amount
        if direction == "forward":
            horizontal += amount
            depth += (amount * aim)

    print(depth * horizontal)

