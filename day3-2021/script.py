with open("data", "r") as file:
    data = file.readlines()
    result = ""
    for i in range(len(data[0])-1):
        count = 0
        for j in range(len(data)):
            count += int(data[j][i])
        if count > len(data)/2:
            result += "1"
        else:
            result += "0"

    print(result)
    snd = ""
    for i in result:
        if i == '0':        
            snd += '1'
        else:
            snd += '0'

    print(int(result, 2) * int(snd,2))
