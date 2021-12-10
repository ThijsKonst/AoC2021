with open('data', 'r') as file:
    errors = []
    for line in file:
        opened=[]
        for char in line:
            if char == '{' or char == '[' or char == '<' or char == '(':
                opened.append(char)
            if char == '}':
                if opened[-1] == '{':
                    opened.pop(-1)
                else:
                    errors.append(char)
                    break
            if char == '>':
                if opened[-1] == '<':
                    opened.pop(-1)
                else:
                    errors.append(char)
                    break
            if char == ']':
                if opened[-1] == '[':
                    opened.pop(-1)
                else:
                    errors.append(char)
                    break
            if char == ')':
                if opened[-1] == '(':
                    opened.pop(-1)
                else:
                    errors.append(char)
                    break
    print(errors.count(')')*3 + errors.count(']')*57 + errors.count('}')*1197 + errors.count('>')*25137)
