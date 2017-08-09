#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
440. K-th Smallest in Lexicographical Order

Given integers n and k, find the lexicographically k-th smallest integer in the range from 1 to n.
Note: 1 ≤ k ≤ n ≤ 109.
Example: 
Input:
n: 13   k: 2

Output:
10

Explanation:
The lexicographical order is [1, 10, 11, 12, 13, 2, 3, 4, 5, 6, 7, 8, 9], so the second smallest number is 10.
"""


def find_kth_number_in_lexicographical_order(n, k):
    """
    :type n: int
    :type k: int
    :rtype: int
    """
    return int(sorted([str(i) for i in list(range(1, n+1))])[k-1])

if __name__ == '__main__':
    print(find_kth_number_in_lexicographical_order(13, 2))
