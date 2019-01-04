def groupCoors(matrix):
    actual_coors = []
    current_coor = start(matrix) #[0, 0]
    actual_coors.append(current_coor)

    possible_coors = cardinal(matrix, current_coor) #[[1, 0], [0, 1]]

    #zero value matrix: zero([[1, 1]], [0, 0]) --> [[0, 1]]
    matrix = zero(matrix, current_coor)

    while possible_coors != []:
        current_coor = possible_coors[0]
        actual_coors.append(current_coor)

        possible_coors = cardinal(matrix, current_coor)
        matrix = zero(matrix, current_coor)

    return actual_coors
