class Entry:
    def __init__(self, number):
        self.passed = False
        self.number = number

    def __str__(self):
        return f"{self.passed}{self.number}" 


    def __repr__(self):
        return f"{self.passed}{self.number}" 

class Field:
    state = []
    def add_line(self, entries):
        self.state.append(entries)

    def mark_number(self, number):
        for i in range(len(self.state)):
            for entry in self.state[i]:
                if entry.number == number:
                    entry.passed = True

    def check_bingo(self):
        if len(self.state) == 0:
            return False
        for i in range(len(self.state)):
            bingo = True
            for entry in self.state[i]:
                if not entry.passed:
                    bingo = False
                    break
            if bingo:
                return True

        for i in range(len(self.state[0])):
            bingo = True
            for j in range(len(self.state[i])):
                if not self.state[i][j].passed:
                    bingo = False
                    break

            if bingo:
                return True

        return False

    def calculate_score(self):
        total = 0
        for i in range(len(self.state)):
            for entry in self.state[i]:
                if not entry.passed:
                    total += entry.number

        return total


    def __str__(self):
        string = ""
        for row in self.state:
            string += row.__str__()
            string += "\n"
        return string

    def __repr__(self):
        string = ""
        for row in self.state:
            string += row.__str__()
            string += "\n"
        return string

with open('data', 'r') as file:
    data = file.readlines()

    bingo_input = data[0]
    print(bingo_input)
    fields = []  
    field = Field()

    for line in data[1:]:
        if line == "\n":
            fields.append(field)
            field = Field()
            field.state=[]

        else:
            row = []
            for entry in line.split(" "):
                if entry != '':
                    row.append(Entry(int(entry)))
            field.add_line(row)

    found = False
    for bingo in bingo_input.split(","):
        bingo = int(bingo)
        for field in fields:
            field.mark_number(bingo)
            if field.check_bingo() and not found:
                print((field.calculate_score() * bingo))
                found = True
