import numpy as np
import helper as h

matrix = np.array([
    [1, 1, 0, 1],
    [1, 0, 1, 1],
    [1, 1, 0, 0],
])
print(matrix)

ONES_COORS = h.ones(matrix)

'''
# full POC
ONES_COORS = h.ones(matrix)
print(ONES_COORS)

while True: # loop to find the cardinal ones of coordinate
    #print(np.array(matrix2))
    print(matrix)
    xcoor = int(input("x coor? "))
    ycoor = int(input("y coor? "))
    cardinal_ones = h.cardinalOnes(ONES_COORS, [xcoor, ycoor])
    print(cardinal_ones)
    print()'''

'''print(matrix)
ONES_COORS = h.ones(matrix)

for i, coor in enumerate(ONES_COORS):
    print(i, ":", coor, h.cardinalOnes(ONES_COORS, coor))'''

# in the output, do you notice a diagonal relationship?
# it continues fully!

# by changing the element at coordinate [1, 1] from a
# one to a zero, we can see this relationship break apart

''' terminal output:
[[1 1 0 1]
 [1 0 1 1]
 [1 1 0 0]]
0 : [0, 0] [[1, 0], [0, 1]]
1 : [1, 0] [[0, 0]]             1 and 0
2 : [3, 0] [[3, 1]]
3 : [0, 1] [[0, 2], [0, 0]]     3 and 1 and 0
4 : [2, 1] [[3, 1]]
5 : [3, 1] [[2, 1], [3, 0]]
6 : [0, 2] [[1, 2], [0, 1]]     6 and 3 and 1 and 0
7 : [1, 2] [[0, 2]]             7 and 6 and 3 and 1 and 0
'''

# therefore: group is [1, 2], [0, 2], [0, 1], [0, 0]
# it's the manhunt algorithm!


def belongsCombine(row1, row2):
    for a in row1:
        for b in row2:
            if a == b:
                return row1 + row2
    else:
        return row1

'''
cardinal_ones = h.cardinalOnes(ONES_COORS, coor)
group = [i for i in cardinal_ones]
group.append(coor)
print(group)
'''

# original group created #
# this should be a function #


def getGroup(ONES_COORS, coor):
    cardinal_ones = h.cardinalOnes(ONES_COORS, coor)
    group = [i for i in cardinal_ones]
    group.append(coor)
    return group


'''
print(getGroup(ONES_COORS, [2, 0]))
[[3, 0], [1, 0], [2, 1], [2, 0]]
'''

# the original reference group
group = getGroup(ONES_COORS, ONES_COORS[0])

for coor in ONES_COORS:
    group_current = getGroup(ONES_COORS, coor)
    group = belongsCombine(group, group_current)
    print(group)

# I got this from stackechange, no idea what is going on
print([list(t) for t in set(tuple(element) for element in group)])
