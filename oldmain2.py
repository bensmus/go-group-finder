import numpy as np
import helper as h

matrix = np.array([
[1, 1, 1, 0],
[0, 0, 1, 1],
[1, 1, 0, 0],
])

ONES_COORS = h.ones(matrix)

current_coor = ONES_COORS[0]; print(current_coor)
actual_coors = [current_coor]; print(actual_coors)
possible_coors = h.cardinalOnes(ONES_COORS, current_coor); print(possible_coors)
matrix = h.passed(matrix, current_coor); print(matrix)

while possible_coors != []:
    current_coor = possible_coors[0]

    actual_coors.append(current_coor)
    possible_coors.remove(current_coor)
    matrix = h.passed(matrix, current_coor)
    print(matrix)

    possible_coors += h.cardinalOnes(matrix, current_coor)
    print(possible_coors)
