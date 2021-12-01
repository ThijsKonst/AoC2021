with open("data", "rt") as file:
    counter = 0
    data = []
    for line in file: 
        data.append(int(line))

    sum_data = []
    for i in range(len(data)):
        if i == len(data) - 2:
            break
        sum_data.append(data[i] + data[i+1] + data[i+2])

    for i in range(len(sum_data)):
        if i == len(sum_data) - 1:
            break
        if sum_data[i] < sum_data[i+1]:
            counter += 1

    print(counter)


