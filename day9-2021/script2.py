import math

def explore(x:int, y:int, list, already_explored):
    if (x, y) in already_explored or (x == len(list) or y == len(list[0])) or list[x][y] == 9:
        return already_explored
    already_explored.append((x, y))
    already_explored = explore(abs(x-1), y, list, already_explored)
    already_explored = explore(x, abs(y-1), list, already_explored)
    already_explored = explore(x+1, y, list, already_explored)
    already_explored = explore(x, y+1, list, already_explored)

    return already_explored


with open('data', 'r') as file:
    data = [[int(y) for y in x.strip()] for x in file.readlines()]
    basin_locations = []
    for i in range(len(data)):
        for j in range(len(data[0])):
            point = data[i][j]
            if i == len(data)-1 and j == len(data[0])-1:
                if data[abs(i-1)][j] > point and data[i][abs(j-1)] > point:
                    basin_locations.append((i,j))
            elif i == len(data)-1:
                if data[abs(i-1)][j] > point and data[i][abs(j-1)] > point and data[i][abs(j+1)] > point:
                    basin_locations.append((i,j))

            elif j == len(data[0])-1:
                if data[abs(i-1)][j] > point and data[i][abs(j-1)] > point and data[abs(i+1)][j] > point:
                    basin_locations.append((i,j))

            elif data[abs(i-1)][j] > point and data[i][abs(j-1)] > point and data[abs(i+1)][j] > point and data[i][abs(j+1)] > point:
                basin_locations.append((i,j))
    
    checklist = [len(explore(location[0], location[1], data, [])) for location in basin_locations]
    checklist.sort()
    print(math.prod([p for p in checklist[-3:]]))
    
