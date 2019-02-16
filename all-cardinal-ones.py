import numpy as np
import helper as h

'''matrix = np.array([
[1, 1, 0, 0],
[0, 0, 1, 1],
[1, 1, 0, 0],
])

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

matrix = np.array([
[1, 1, 0, 0],
[0, 1, 1, 1]
]); print(matrix)

ONES_COORS = h.ones(matrix)

for coor in ONES_COORS:
    print(coor, h.cardinalOnes(ONES_COORS, coor))

    # in the output, do you notice a diagonal relationship?
    # it continues fully!

    # by changing the element at coordinate [1, 1] from a
    # one to a zero, we can see this relationship break apart
