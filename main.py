import numpy as np
import helper as h

matrix = np.array([
    [int(input("1 or 0: ")) for i in range(4)] for i in range(3)
])

print()
print(matrix)
print()


def belongsCombine(row1, row2):
    for a in row1:
        for b in row2:
            if a == b:
                return row1 + row2
    else:
        return row1


def getGroup(ONES_COORS, coor):
    cardinal_ones = h.cardinalOnes(ONES_COORS, coor)
    group = [i for i in cardinal_ones]
    group.append(coor)
    return group


ONES_COORS = h.ones(matrix)
# the original reference group
group = getGroup(ONES_COORS, ONES_COORS[0])

for coor in ONES_COORS:
    group_current = getGroup(ONES_COORS, coor)
    group = belongsCombine(group, group_current)

# remove duplicates
group = [list(t) for t in set(tuple(element) for element in group)]

# print a matrix that shows the found group
for coor in group:
    matrix = h.passed(matrix, coor)
print(matrix)
