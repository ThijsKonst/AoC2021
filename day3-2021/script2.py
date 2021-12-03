with open("data", "r") as file:
    data = file.readlines()
    working_data = data
    for i in range(len(data[0])-1):
        count = 0
        ones = []
        zeroes = []

        for j in range(len(working_data)):
            count += int(working_data[j][i])

            if working_data[j][i] == '0':
                zeroes.append(working_data[j])
            else:
                ones.append(working_data[j])

        if count >= len(working_data)/2:
            working_data = ones
        else:
            working_data = zeroes
        if len(working_data) == 1:
            result_most = working_data[0]
            break
    
    working_data = data
    for i in range(len(data[0])-1):
        count = 0
        ones = []
        zeroes = []

        for j in range(len(working_data)):
            count += int(working_data[j][i])

            if working_data[j][i] == '0':
                zeroes.append(working_data[j])
            else:
                ones.append(working_data[j])

        if count < len(working_data)/2:
            working_data = ones
        else:
            working_data = zeroes
        if len(working_data) == 1:
            result_least = working_data[0]
            break

    print(int(result_most, 2) * int(result_least,2))
    
