#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
542. 01 Matrix

Given a matrix consists of 0 and 1, find the distance of the nearest 0 for each cell.
The distance between two adjacent cells is 1.
Example 1:
Input:
0 0 0
0 1 0
0 0 0
Output:
0 0 0
0 1 0
0 0 0

Example 2:
Input:
0 0 0
0 1 0
1 1 1
Output:
0 0 0
0 1 0
1 2 1

Note:
The number of elements of the given matrix will not exceed 10,000.
There are at least one 0 in the given matrix.
The cells are adjacent in only four directions: up, down, left and right.
"""


def find_path(matrix):
    """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
    """
    matrix_size = len(matrix)
    new_matrix = []
    for x in range(matrix_size):
        row = []
        for y in range(matrix_size):
            up, down, left, right = 1, 1, 1, 1
            if x > 0:
                up = matrix[x-1][y]
            if x < matrix_size - 1:
                down = matrix[x+1][y]
            if y > 0:
                left = matrix[x][y-1]
            if y < matrix_size - 1:
                right = matrix[x][y+1]
            if all([up, down, left, right]):
                row.append(matrix[x][y]+1)
            else:
                row.append(matrix[x][y])
        new_matrix.append(row)
    return new_matrix

if __name__ == '__main__':
    print(find_path([[1,1,1],[0,1,0],[0,0,0]]))
