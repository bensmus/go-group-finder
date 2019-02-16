import numpy as np


def passed(matrix, coordinate):
    matrix[coordinate[1]][coordinate[0]] = 8
    return matrix


def ones(matrix):
    '''get a matrix with all of the ones'''
    onesMatrix = []
    for y, row in enumerate(matrix):
        for x, elem in enumerate(row):
            if elem == 1:
                onesMatrix.append([x, y])
    return onesMatrix


def cardinal(coordinate):
    cardinal_coors = []
    cardinal_coors.append([coordinate[0] + 1, coordinate[1]])
    cardinal_coors.append([coordinate[0] - 1, coordinate[1]])
    cardinal_coors.append([coordinate[0], coordinate[1] + 1])
    cardinal_coors.append([coordinate[0], coordinate[1] - 1])
    return cardinal_coors


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


def getGroup(ONES_COORS, coor):
    cardinal_ones = cardinalOnes(ONES_COORS, coor)
    group = [i for i in cardinal_ones]
    group.append(coor)
    return group


def belongsTest(group, test_group):
    for a in group:
        for b in test_group:
            if a == b:
                return True

    return False


matrix = np.array([
    [int(input("1 or 0: ")) for i in range(4)] for i in range(3)
])

print()
print(matrix)
print()


ONES_COORS = ones(matrix)
groups = []

for coor in ONES_COORS:
    groups.append(getGroup(ONES_COORS, coor))

print(np.array(groups))
print()

shape = [groups[0]]
groups.pop(0)

print("shape:  ", shape)
print("groups: ", groups)
print()

'''we will be adding groups to the shape, and removing them from the group'''
'''the idea is correct, but we need to run it twice to fix that bug'''
for i in range(2):
    for group in shape:
        for test_group in groups:
            if belongsTest(group, test_group):
                shape.append(test_group)
                groups.remove(test_group)
                print("shape:  ", shape)
                print("groups: ", groups)
                print()

'''
# remove duplicates
group = [list(t) for t in set(tuple(element) for element in group)]

# print a matrix that shows the found group
for coor in group:
    matrix = passed(matrix, coor)
print(matrix)
'''
'''
woah! a bug?
[[0 0 0 1]
 [1 1 1 1]
 [1 1 0 0]]

[[0 0 0 8]
 [1 8 8 8]
 [8 8 0 0]]
'''
'''
another one!
[[0 0 0 1]
 [1 1 1 1]
 [1 0 0 0]]

[[0 0 0 8]
 [1 8 8 8]
 [1 0 0 0]]
'''
