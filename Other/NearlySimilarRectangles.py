"""
Recently,
while researching about similar rectangles, you found the term "Nearly Similar Rectangle." Two rectangles with sides (a,b) and (c,d) are nearly
similar only if a/c = b/d. The order of sides matter in this definition, so rectangles [4, 2] and [6, 3] are nearly similar, but rectangles [2,4]
and [6,3] are not. Given an array of rectangles with the length of their sides, calculate the number of pairs of nearly similar rectangles in the array.

For example, let's say there are n = 4 rectangles,
and sides = [[5, 10], [10,10], [3,6], [9,9]]. In this case, the first and third rectangles, with sides [5, 10] and [3,6], are
nearly similar because 5/3 = 10/6. Also, the second and fourth rectangles, with sides [10, 10] and [9, 9], are nearly similar because
10/9 = 10/9. This means there are 2 pairs of nearly similar rectangles in the array. Therefore, the answer is 2.

Function Description:
Complete the function nearlySimilarRectangles in the editor below.
nearlySimilarRectangles has following parameters:

int sides[n][2]: a 2-dimesnional; integer array where the i^th row denotes the sides of the i^th rectangle.
Returns:
    int: the number of nearly similar rectangles in the array

Constraints

> 1<= n <= 10**5
> 1<=sides[i][0], sides[i][1]<=10**15

Input Format:
The first line contains an integer, n, denoting the number of rows in sides.

The next line contains and integer, 2, denoting the number of columns in sides.

Each line i of the n subsequent lines (where 0 <= i< n) contains 2 space-separated
integers, sides[i][0] and sides[i][1], denoting the lengths of ith rectangles's sides.

"""


def nearlySimilarRectangles(sides):
    LONG_INTEGER = 0
    for i in range(len(sides)):
        x = sides[i]
        for j in range(i + 1, len(sides)):
            y = sides[j]
            if x[0] / y[0] == x[1] / y[1]:
                LONG_INTEGER += 1

    return int(LONG_INTEGER)


print(nearlySimilarRectangles([[5, 10], [10, 10], [3, 6], [9, 9]]))
print(nearlySimilarRectangles([[4, 8], [15, 30], [25, 50]]))
