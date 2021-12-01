with open("data", "rt") as file:
    for line in file:
        complement = 2020 - int(line)
        with open("data", "rt") as file2:
            for line2 in file2:
                if complement == int(line2):
                    print(int(line) * int(line2))
    print("not cracked")


