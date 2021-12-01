with open("data", "rt") as file:
    counter = 0
    data = file.readlines()

    for i in range(len(data)-1):
        if int(data[i]) < int(data[i+1]):
            counter += 1
    
    print(counter)


