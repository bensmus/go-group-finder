import numpy as np
import random as rm

'''this program is based on trying to find clusters of connected
stones in the game "go".
Stones of a certain color are modelled as ones
in a 2d matrix and everything else as zeroes'''

'''Program generates a random matrix of ones and zeroes and then
changes the first "1" it finds (scanning from top left) and all
of the "1"'s connected to it (according to the rules of go) into
"8"'s'''

def passed(matrix, coordinate):
    '''function changes matrix element into an 8'''
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
    '''used to find "cardinal ones"'''
    cardinal_coors = []
    cardinal_coors.append([coordinate[0] + 1, coordinate[1]])
    cardinal_coors.append([coordinate[0] - 1, coordinate[1]])
    cardinal_coors.append([coordinate[0], coordinate[1] + 1])
    cardinal_coors.append([coordinate[0], coordinate[1] - 1])
    return cardinal_coors


def matrixAnd(matrix1, matrix2):
    '''used to find "cardinal ones" '''
    bothMatrix = []
    for row1 in matrix1:
        for row2 in matrix2:
            if row1 == row2:
                bothMatrix.append(row1)
    return bothMatrix


def cardinalOnes(ONES_COORS, coordinate):
    '''cardinal ones are a set of "1" elements surrounding
    a certain coordinate (adjacent to the coordinate
    by one step in the cardinal direction) '''

    cardinal_coors = cardinal(coordinate)
    cardinal_ones = matrixAnd(cardinal_coors, ONES_COORS)
    return cardinal_ones


def getGroup(ONES_COORS, coor):
    '''a group is formed of cardinal ones and
    their source coordinate'''
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


def _3d_2d(_3d):
    '''turn a 3d array into a 2d array
    join cardinal groups together'''
    _2d = []
    d = len(_3d)
    for i in range(d):
        # some 2d matrices (cardinal groups) are larger than others...
        for j in range(len(_3d[i])):
            _2d.append(_3d[i][j])
    return _2d


# 1: Make a random matrix containing zeroes and ones

matrix = np.array([
    [rm.randint(0, 1) for i in range(10)] for i in range(10)
])

print(matrix)
print()

# 2: Get all of the cardinal groups (sets of 2, 3 or 4 ones)
# that are in horizontal or vertical adjacency

ONES_COORS = ones(matrix)
groups = []

for coor in ONES_COORS:
    groups.append(getGroup(ONES_COORS, coor))


# start group
shape = [groups[0]]
groups.pop(0)

# 3: Look at which of these cardinal groups have a common element

# we will be adding group to "shape", and removing group from "groups"
for group in shape:
    for test_group in groups:
        if belongsTest(group, test_group):
            shape.append(test_group)
            groups.remove(test_group)

shape = _3d_2d(shape)

# 4: Represent the first combination of cardinal groups as
# eights on the matrix

# remove duplicates in the 2d array
shape = [list(t) for t in set(tuple(element) for element in shape)]

# print a matrix that shows the found group
for coor in shape:
    matrix = passed(matrix, coor)
print(matrix)
