#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
593. Valid Square

Given the coordinates of four points in 2D space, return whether the four points could construct a square.
The coordinate (x,y) of a point is represented by an integer array with two integers.
Example:
Input: p1 = [0,0], p2 = [1,1], p3 = [1,0], p4 = [0,1]
Output: True

Note:
All the input integers are in the range [-10000, 10000].
A valid square has four equal sides with positive length and four equal angles (90-degree angles).
Input points have no order.
"""
from itertools import combinations


def valid_square(p1, p2, p3, p4):
    """
        :type p1: List[int]
        :type p2: List[int]
        :type p3: List[int]
        :type p4: List[int]
        :rtype: bool
    """
    return len(set([(lambda a, b: (a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)(i, j)
                    for i, j in list(combinations([p1, p2, p3, p4], 2))])) == 2


if __name__ == '__main__':
    print(valid_square([0,0], [1,1], [1,0], [0,1]))
