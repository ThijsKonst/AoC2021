import pandas as pd

with open("data", "r") as file:
    data = file.readlines()
    coords = []
    for line in data:
        first, second = line.split(" -> ")
        x1, y1 = first.split(",")
        x1 = int(x1)
        y1 = int(y1)
        x2, y2 = second.split(",")
        x2 = int(x2)
        y2 = int(y2)
        if x1 == x2:
            if y2 > y1:
                for i in range(y1, y2+1):
                    coords.append((x1, i))
            else: 
                for i in range(y2, y1+1):
                    coords.append((x1, i))
        if y1 == y2:
            if x2 > x1:
                for i in range(x1, x2+1):
                    coords.append((i, y1))
            else:
                for i in range(x2, x1+1):
                    coords.append((i, y1))

    counts = pd.Series(coords).value_counts()
    i = 0
    for entry in counts:
        if int(entry) >= 2:
            i += 1

    print(i)
