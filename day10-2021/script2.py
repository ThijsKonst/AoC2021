with open('data', 'r') as file:
    scores = []
    for line in file:
        opened=[]
        for char in line:
            if char == '{' or char == '[' or char == '<' or char == '(':
                opened.append(char)
            if char == '}':
                if opened[-1] == '{':
                    opened.pop(-1)
                else:
                    opened = []
                    break
            if char == '>':
                if opened[-1] == '<':
                    opened.pop(-1)
                else:
                    opened = []
                    break
            if char == ']':
                if opened[-1] == '[':
                    opened.pop(-1)
                else:
                    opened = []
                    break
            if char == ')':
                if opened[-1] == '(':
                    opened.pop(-1)
                else:
                    opened = []
                    break
        if opened != []:
            count = 0
            for char in opened[::-1]:
                count *= 5            
                if char == '(':
                    count += 1
                elif char == '[':
                    count += 2
                elif char == '{':
                    count += 3
                elif char == '<':
                    count += 4

            scores.append(count)
    
    print(len(scores))
    print(len(scores)/2 + 0.5)
    scores.sort()
    print(scores)
    print(scores[int(len(scores)/2+0.5) - 1])
