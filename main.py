import helper as h # start, passed, cardinalOnes

def groupCoors(matrix):
    actual_coors = []

    current_coor = h.start(matrix) #[0, 0]
    actual_coors.append(current_coor)

    # 8 value matrix: passed([[1, 1]
    #                         [0, 1]], [0, 0]) --> [[8, 1]
    #                                               [0, 1]]
    matrix = h.passed(matrix, current_coor)
    print(matrix)

    possible_coors = h.cardinalOnes(matrix, current_coor)
    # possible_coors will be [[1, 0], [0, 1]], assuming both are one valued

    while possible_coors != []:
        current_coor = possible_coors[0]
        actual_coors.append(current_coor)

        matrix = h.passed(matrix, current_coor)
        print(matrix)

        possible_coors.remove(current_coor)
        possible_coors += h.cardinalOnes(matrix, current_coor)

    return actual_coors

matrix = [
[1, 1, 1, 0],
[0, 0, 1, 1],
[1, 1, 0, 0],
]

actual_coors = groupCoors(matrix)
print(actual_coors)
