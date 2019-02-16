import numpy as np
import random as rm


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


'''def crunch3d2d(array):
    crunched = []
    for x in array:
        for y in array:
            crunched.append(y)
    return crunched <-- fail'''


def _3d_2d(_3d):
    _2d = []
    d1 = len(_3d)
    d2 = len(_3d[0])
    for i in range(d1):
        for j in range(d2):
            _2d.append(_3d[i][j])
    return _2d


matrix = np.array([
    [rm.randint(0, 1) for i in range(6)] for i in range(6)
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
'''lets not run it twice, but find a better way to fix it'''

for group in shape:
    for test_group in groups:
        if belongsTest(group, test_group):
            shape.append(test_group)
            groups.remove(test_group)
            print("shape:  ", shape)
            print("groups: ", groups)
            print()

shape = _3d_2d(shape)

# remove duplicates in the 2d array
shape = [list(t) for t in set(tuple(element) for element in shape)]

# print a matrix that shows the found group
for coor in shape:
    matrix = passed(matrix, coor)
print(matrix)

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
'''
In [2]: def _3d_2d(_3d):
   ...:     converts 3d array to a 2d one
   ...:     _2d = []
   ...:     d1 = len(_3d)
   ...:     d2 = len(_3d[0])
   ...:     for i in range(d1):
   ...:         for j in range(d2):
   ...:             _2d.append(_3d[i][j])
   ...:     return _2d
   ...:

In [3]: _3d = [
   ...: [[0, 1],
   ...:  [1, 1]],
   ...:
   ...: [[1, 1],
   ...:  [2, 1]]
   ...: ]

In [4]: _2d = _3d_2d(_3d)

In [5]: _2d
Out[5]: [[0, 1], [1, 1], [1, 1], [2, 1]]

In [6]:
IPython testing to get _3d_2d function '''
