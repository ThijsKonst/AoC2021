with open('data', 'r') as file:
    fishes = [int(x) for x in file.readlines()[0].split(',')]
    fishes = [fishes.count(0), fishes.count(1), fishes.count(2), fishes.count(3), fishes.count(4), fishes.count(5), fishes.count(6), fishes.count(7), fishes.count(8)]
    i = 0
    while i < 256:
        newfishes = fishes.pop(0)
        fishes[6] += newfishes
        fishes.append(newfishes)
        i += 1
    print(sum(fishes))
