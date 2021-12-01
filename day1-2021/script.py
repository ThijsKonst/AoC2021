with open("data", "rt") as file:
    counter = 0
    data = []
    for line in file: 
        data.append(int(line))

    for i in range(len(data)):
        if i == len(data) - 1:
            break
        if data[i] < data[i+1]:
            counter += 1
    
    print(counter)


