with open('data', 'r') as file:
    data = [int(x) for x in file.readline().split(',')]
    lowest_cost = 1000000000000
    for x in range(min(data), max(data)+1):
        if (cost := sum([sum(range(abs(x-y) + 1)) for y in data])) < lowest_cost:
            lowest_cost = cost
    print(lowest_cost)

