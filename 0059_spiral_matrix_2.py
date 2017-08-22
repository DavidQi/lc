#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
59. Spiral Matrix II

Given an integer n, generate a square matrix filled with elements from 1 to n2 in spiral order.
For example,
Given n = 3,
You should return the following matrix:
[
 [ 1, 2, 3 ],
 [ 8, 9, 4 ],
 [ 7, 6, 5 ]
]
"""


def spiral_clockwise(n):
    # | | => |9| => |8| => |6 7| => |4 5| => |1 2 3|
    #               |9|    |9 8|    |9 6|    |8 9 4|
    #                               |8 7|    |7 6 5|
    current = n * n
    rows = [[current]]
    while current > 1:
        current -= len(rows)
        rows = [list(range(current, current + len(rows)))] + list(zip(*rows[::-1]))
    return rows
print('\n'.join([str(_) for _ in spiral_clockwise(3)]))


def spiral_anti_clockwise(n):
    # | | => |9| => |8 9| => |6 9| => |4 9 8| => |1 8 7|
    #                        |7 8|    |5 6 7|    |2 9 6|
    #                                            |3 4 5|
    current = n * n
    rows = [[current]]
    while current > n:
        current -= len(rows)
        rows = list(zip(*([list(range(current, current - len(rows[0]), -1))] + rows)))[::-1]
    return rows
print('\n'.join([str(_) for _ in spiral_anti_clockwise(3)]))

