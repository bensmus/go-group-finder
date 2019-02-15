import helper as h
import numpy as np #for pretty matrix printing

matrix1 = [
[1, 1, 1, 0],
[0, 0, 1, 1],
[1, 1, 0, 0],
]

matrix2 = [
[0, 1, 1, 0],
[1, 0, 1, 1],
[1, 1, 0, 0],
]

# GET X, Y COORDINATES OF THE FIRST 1 ELEMENT IN THE MATRIX
# print(h.start(matrix1)) OK
# print(h.start(matrix2)) OK

# TURN AN ELEMENT TO AN 8 TO INDICATE THAT IT IS PART OF THE GROUP
'''the whole point is that we are not just looking for all the ones,
but just for the ones that are part of a group. These turn into eights'''
# h.passed(matrix1, h.start(matrix1)) OK
# print(matrix1) OK

# FIND THE CARDINAL COORDINATES
'''from a coordinate [x, y] we get a matrix of four coordinates'''
# print(h.cardinal(h.start(matrix1))) OK
# print(h.cardinal(h.start(matrix2))) OK

# NOW THE COORDINATES NEED TO PASS TWO TESTS:
# 1. THEY ARE IN THE MATRIX (NO NEGATIVE VALUES)
# 2. THEY CORRESPOND TO A 1 ELEMENT

# print(h.cardinalOnes(matrix2, [1, 1])) OK
# print(h.cardinalOnes(matrix2, [0, 0])) OK
# print(h.cardinalOnes(matrix2, [2, 2])) FAILED!

'''
ben@ben-VirtualBox:~/python/group-finder$ python3 tests.py
[[2, 1], [0, 1], [1, 2], [1, 0]]
[[1, 0], [0, 1]]
Traceback (most recent call last):
  File "tests.py", line 36, in <module>
    print(h.cardinalOnes(matrix2, [2, 2]))
  File "/home/ben/python/group-finder/helper.py", line 15, in cardinalOnes
    final_coors = final(matrix, positive_coors)
  File "/home/ben/python/group-finder/helper.py", line 38, in final
    if matrix[coordinate[1]][coordinate[0]] != 1:
IndexError: list index out of range
'''

# cardinal_coors = h.cardinal([2, 2])
# print(cardinal_coors)
# positive_coors = h.positive(cardinal_coors)

# haha! we should not only be checking for the positive ones,
# but also for the indexes out of range (bigger than the matrix)
# print(positive_coors) #[2, 3] should NOT BE A VALID COORDINATE!

'''
new approach:
start by getting all of the coordinates of the ones: filter
from there. This way positive filter can be discarded.
'''
'''
print(h.ones(matrix1))
print(h.cardinal([0, 0]))

# make a intersection function for matrices!
A = [
[1, 2, 3],
[5, 6, 7],
[4, 5, 6]
]

B = [
[1,2,3],
[5,6,7]
]
print(h.matrixAnd(A, B))
'''

# full test
ONES_COORS = h.ones(matrix2)
print(ONES_COORS)

while True: # loop to find the cardinal ones of coordinate
    print(np.array(matrix2))
    xcoor = int(input("x coor? "))
    ycoor = int(input("y coor? "))
    cardinal_ones = h.cardinalOnes(ONES_COORS, [xcoor, ycoor])
    print(cardinal_ones)
    print()
