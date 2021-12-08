with open('data', 'r') as file:
    data = [x.split('|')[1] for x in file.readlines()]
    count = 0 
    for line in data:
        for num in line.split(' '):
            num = num.strip()
            if len(num) == 2 or len(num) == 3 or len(num) == 4 or len(num) == 7:
                count+=1
    print(count)
