'''def start(matrix):
    for y, array in enumerate(matrix):
        for x, elem in enumerate(array):
            if elem == 1:
                return [x, y]'''


def ones(matrix):
    '''get a matrix with all of the ones'''
    onesMatrix = []
    for y, row in enumerate(matrix):
        for x, elem in enumerate(row):
            if elem == 1:
                onesMatrix.append([x, y])
    return onesMatrix


def passed(matrix, coordinate):
    matrix[coordinate[1]][coordinate[0]] = 8
    return matrix


def cardinal(coordinate):
    cardinal_coors = []
    cardinal_coors.append([coordinate[0] + 1, coordinate[1]])
    cardinal_coors.append([coordinate[0] - 1, coordinate[1]])
    cardinal_coors.append([coordinate[0], coordinate[1] + 1])
    cardinal_coors.append([coordinate[0], coordinate[1] - 1])
    return cardinal_coors

# make a intersection function for matrices!
# if in cardinal and in ones... cardinal ones!

def matrixAnd(matrix1, matrix2):
    bothMatrix = []
    for row1 in matrix1:
        for row2 in matrix2:
            if row1 == row2:
                bothMatrix.append(row1)
    return bothMatrix

def cardinalOnes(ONES_COORS, coordinate):
    cardinal_coors = cardinal(coordinate)
    cardinal_ones = matrixAnd(cardinal_coors, ONES_COORS)
    return cardinal_ones


'''def positive(cardinal_coors):
    for coordinate in cardinal_coors:
        for value in coordinate:
            if value < 0:
                cardinal_coors.remove(coordinate)
    return cardinal_coors'''


'''def final(matrix, positive_coors):
    for coordinate in positive_coors:
        if matrix[coordinate[1]][coordinate[0]] != 1:
            positive_coors.remove(coordinate)
    return positive_coors'''


'''def cardinalOnes(matrix, coordinate):
    cardinal_coors = cardinal(coordinate)
    positive_coors = positive(cardinal_coors)
    final_coors = final(matrix, positive_coors)
    return final_coors'''

# this is used so that when this module is imported,
# all of the subtests dont run and the output of this program
# is mixed in with the output of the previous program
if __name__ == "main":
    matrix = [
        [1, 1, 1, 0],
        [0, 0, 1, 1],
        [1, 1, 0, 0],
    ]

    print(start(matrix))

    passed(matrix, [1, 1])
    print(matrix)

    cardinalOnes(matrix, [0, 0])
