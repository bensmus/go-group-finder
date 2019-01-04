def start(matrix):
    for y, array in enumerate(matrix):
        for x, elem in enumerate(array):
            if elem == 1:
                return [x, y]

matrix = [
[1, 1, 1, 0],
[0, 0, 1, 1],
[1, 1, 0, 0],
]

print(start(matrix))

def passed(matrix, coordinate):
    matrix[coordinate[1]][coordinate[0]] = 8

passed(matrix, [1, 1])
print(matrix)

def cardinalOnes(matrix, coordinate):
    cardinal_coors = cardinal(coordinate)
    positive_coors = positive(cardinal_coors)
    final_coors = final(matrix, positive_coors)
    return final_coors

def cardinal(coordinate):
    cardinal_coors = []
    cardinal_coors.append([coordinate[0] + 1, coordinate[1]])
    cardinal_coors.append([coordinate[0] - 1, coordinate[1]])
    cardinal_coors.append([coordinate[0], coordinate[1] + 1])
    cardinal_coors.append([coordinate[0], coordinate[1] - 1])
    return cardinal_coors

def positive(cardinal_coors):
    for coordinate in cardinal_coors:
        for value in coordinate:
            if value < 0:
                cardinal_coors.remove(coordinate)
    return cardinal_coors

def final(matrix, positive_coors):
    for coordinate in positive_coors:
        if matrix[coordinate[1]][coordinate[0]] != 1:
            positive_coors.remove(coordinate)
    return positive_coors

cardinalOnes(matrix, [0, 0])
