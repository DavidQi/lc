#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
152. Maximum Product Subarray

Find the contiguous subarray within an array (containing at least one number) which has the largest product.
For example, given the array [2,3,-2,4],
the contiguous subarray [2,3] has the largest product = 6.
"""


from functools import reduce


class Solution(object):
    def __init__(self):
        self.max, self.sub_array = 0, []

    def max_product(self, nums):
        """
        :type nums: List[int]
        """
        self.max = max(nums)
        self.sub_array = [self.max]
        for i, _ in enumerate(nums):
            for j in range(2, len(nums)):
                m = reduce(lambda x, y: x*y, nums[i:i+j])
                if m > self.max:
                    self.max = m
                    self.sub_array = nums[i:i+j]


def max_product_only(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    return max([reduce(lambda x, y: x*y, nums[i:i+j]) for i in range(len(nums)) for j in range(2, len(nums))])


if __name__ == '__main__':
    test_array = [2, 3, -2, 4, 6]
    o = Solution()
    o.max_product(test_array)
    print('The contiguous subarray %s has the largest product = %d. ' % (str(o.sub_array), o.max))
    print(max_product_only(test_array))
