#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
Given an integer, return its base 7 string representation.
Example 1:
Input: 100
Output: "202"

Example 2:
Input: -7
Output: "-10"

Note: The input will be in range of [-1e7, 1e7].
"""


def convert_2_base7(num):
    """
        :type num: int
        :rtype: str
    """
    def base7(n):
        return [str(n)] if n < 7 else base7(n//7) + [str(n % 7)]
    return '-' * (num < 0) + ''.join(base7(abs(num)))

if __name__ == '__main__':
    print(convert_2_base7(-100))
