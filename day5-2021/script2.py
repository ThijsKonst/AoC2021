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

        elif y1 == y2:
            if x2 > x1:
                for i in range(x1, x2+1):
                    coords.append((i, y1))
            else:
                for i in range(x2, x1+1):
                    coords.append((i, y1))
        else:
            range1 = range(x1, x2+1) if x2>x1 else range(x2, x1+1)[::-1]
            range2 = range(y1, y2+1) if y2>y1 else range(y2, y1+1)[::-1]
            for i in range(len(range1)):
                coords.append((range1[i], range2[i]))

    counts = pd.Series(coords).value_counts()
    j = 0
    for entry in counts:
        if int(entry) >= 2:
            j += 1

    print(j)
