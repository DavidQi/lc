#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
198. House Robber

You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed,
the only constraint stopping you from robbing each of them is that adjacent houses have security system connected and
it will automatically contact the police if two adjacent houses were broken into on the same night.
Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of
money you can rob tonight without alerting the police.
"""


def nonadjacent_max_sum(nums):
    """
        :type nums: List[int]
        :rtype: int
    """
    sorted_list = sorted(enumerate(nums), key=lambda i: i[1], reverse=True)
    if abs(sorted_list[0][0] - sorted_list[1][0]) != 1:  # 0 & 1 are nonadjacent
        return sorted_list[0][0], sorted_list[1][0]
    else:
        if abs(sorted_list[0][0] - sorted_list[2][0]) != 1:  # 0 & 2 are nonadjacent
            return sorted_list[0][0], sorted_list[2][0]
        else:  # check 3
            if abs(sorted_list[1][0] - sorted_list[2][0]) != 1:  # 1 & 2 are nonadjacent, will compare
                if sorted_list[1][1] + sorted_list[2][1] > sorted_list[0][1] + sorted_list[3][1]:
                    return sorted_list[1][0], sorted_list[2][0]
            return sorted_list[0][0], sorted_list[3][0]


if __name__ == '__main__':
    import random
    l = random.sample(range(0, 100000), 20)
    print(nonadjacent_max_sum(l))

