input: matrix of ones and zeroes, containing groups of ones
output: coordinates of the groups of ones

Example:
input:
[[1, 1, 1, 0]
 [0, 0, 1, 1]
 [1, 1, 0, 0]]

output:
[[[0, 0], [1, 0], [2, 0], [2, 1], [3, 1], [4, 1]]
 [[0, 2], [1, 2]]]

Steps:

1. Get coordinates of ones

2. Start at first one

3a. Get a list of potential cardinal direction coordinates relative to that first one

3b. Note that for (0, 0), these will be (1, 0), (-1, 0), (0, 1), (0, -1). Discard the coordinates containing negative

4a. Get a list of positions of ones in the accepted cardinal direction coordinates

4b. Choose the first one of the possible ones.

5. Now remove this one from the possible and place into actual.

6. Repeat 3 to 5 while there are possible ones (list not empty)

7. Return actual
