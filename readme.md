input: matrix of ones and zeroes, containing groups of ones
output: coordinates of the groups of ones

Example:
input:
[[1, 1, 1, 0]
 [0, 0, 1, 1]
 [1, 1, 0, 0]]

output:
[[0, 0], [1, 0], [2, 0], [2, 1], [3, 1], [4, 1]]

Steps:

2. Start at first one, add its coordinates to actual

2b. Transform the first one into a zero: it is no longer needed.

3. Get a list of potential cardinal direction coordinates relative to that first one/first possible, and remove the ones that are zeroes

3b. Note that for (0, 0), these will be (1, 0), (-1, 0), (0, 1), (0, -1). Discard the coordinates containing negative

6. Repeat 3 to 4 while there are possible ones (list not empty)

7. Return actual
