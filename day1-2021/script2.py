with open("data", "rt") as file:
    counter = 0
    data = file.readlines()

    sum_data = [int(data[i]) + int(data[i+1]) + int(data[i+2]) for i in range(len(data)-2)]

    for i in range(len(sum_data)-1):
        if sum_data[i] < sum_data[i+1]:
            counter += 1
    print(counter)


