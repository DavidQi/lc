#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
54. Spiral Matrix

Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.
For example,
Given the following matrix:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
You should return [1,2,3,6,9,8,7,4,5].
"""


def spiral_pop(matrix):
    """
    :type matrix: List[List[int]]
    :rtype: List[int]
    """
    # loop at
    # a, pop top row
    # b, rotate 90 degrees counter-clockwise
    return list(matrix.pop(0)) + spiral_pop(list(zip(*matrix))[::-1]) if matrix else []


print(spiral_pop([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]))

