with open('data', 'r') as file:
    data = [[int(y) for y in x.strip()] for x in file.readlines()]
    risk_levels = []
    for i in range(len(data)):
        for j in range(len(data[0])):
            point = data[i][j]
            if i == len(data)-1 and j == len(data[0])-1:
                if data[abs(i-1)][j] > point and data[i][abs(j-1)] > point:
                    risk_levels.append(1 + point)
            elif i == len(data)-1:
                if data[abs(i-1)][j] > point and data[i][abs(j-1)] > point and data[i][abs(j+1)] > point:
                    risk_levels.append(1 + point)

            elif j == len(data[0])-1:
                if data[abs(i-1)][j] > point and data[i][abs(j-1)] > point and data[abs(i+1)][j] > point:
                    risk_levels.append(1 + point)

            elif data[abs(i-1)][j] > point and data[i][abs(j-1)] > point and data[abs(i+1)][j] > point and data[i][abs(j+1)] > point:
                risk_levels.append(1 + point)

    print(sum(risk_levels))
