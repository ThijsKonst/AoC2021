with open('data', 'r') as file:
    data = [x.split('|') for x in file.readlines()]
    counter = 0
    for line in data:
        fline = ""
        digits = {
            '1':"",
            '2':"",
            '3': "",
            '4': "",
            '5': "",
            '6': "",
            '7': "",
            '8': "",
            '9': "",
            '0': "",
        }
        done = False
        while not done:
            for word in line[0].split(" "):
                word = "".join(sorted(word.strip()))
                if len(word) == 2:
                    digits['1'] = word
                elif len(word) == 3:
                    digits['7'] = word
                elif len(word) == 4:
                    digits['4'] = word
                elif len(word) == 7:
                    digits['8'] = word
                elif len(word) == 5:
                    if len(digits['1']) > 0 and set(digits['1']) <= set(word):
                        digits['3'] = word
                    elif len(fline) > 0 and fline in word:
                        digits['5'] = word
                    elif len(fline) > 0:
                        digits['2'] = word
                elif len(word) == 6:
                    if len(digits['1']) > 0 and not set(digits['1']) <= set(word):
                        digits['6'] = word
                        if digits['1'][0] in digits['6']:
                            fline = digits['1'][0]
                        else:
                            fline = digits['1'][1]
                    elif len(digits['4']) > 0 and set(digits['4']) <= set(word):
                        digits['9'] = word
                    elif len(digits['4']) > 0:
                        digits['0'] = word
            done = True
            for digit in digits.values():
                if len(digit) == 0:
                    done = False
        inv_map = {v: k for k, v in digits.items()}
        code = ""
        for word in line[1].split(" "):
            word = "".join(sorted(word.strip()))
            if len(word) > 0:
                code += inv_map[word]
        counter += int(code)
    print(counter)
