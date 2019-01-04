import helper as h #start, zero, cardinalOnes

def groupCoors(matrix):
    actual_coors = []

    current_coor = h.start(matrix) #[0, 0]
    actual_coors.append(current_coor)
    #zero value matrix: zero([[1, 1]], [0, 0]) --> [[0, 1]]
    matrix = h.zero(matrix, current_coor)

    possible_coors = h.cardinalOnes(matrix, current_coor)
    #possible_coors will be [[1, 0], [0, 1]], assuming both are one valued

    while possible_coors != []:
        current_coor = possible_coors[0]
        actual_coors.append(current_coor)
        possible_coors.remove(current_coor)

        matrix = h.zero(matrix, current_coor)
        possible_coors += h.cardinalOnes(matrix, current_coor)

    return actual_coors

matrix = [
[1, 1, 1, 0]
[0, 0, 1, 1]
[1, 1, 0, 0]
]

print(groupCoors(matrix))
