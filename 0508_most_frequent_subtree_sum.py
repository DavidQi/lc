#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
508. Most Frequent Subtree Sum

Given the root of a tree, you are asked to find the most frequent subtree sum.
The subtree sum of a node is defined as the sum of all the node values formed by the subtree rooted at that node
(including the node itself). So what is the most frequent subtree sum value?
If there is a tie, return all the values with the highest frequency in any order.
Examples 1
Input:
  5
 /  \
2   -3
return [2, -3, 4], since all the values happen only once, return all of them in any order.

Examples 2
Input:
  5
 /  \
2   -5
return [2], since 2 happens twice, however -5 only occur once.

Note: You may assume the sum of values in any subtree is in the range of 32-bit signed integer.
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def __init__(self):
        self.dic_results = {}

    def count(self, n):
        if n in self.dic_results:
            self.dic_results[n] += 1
        else:
            self.dic_results[n] = 1

    def most_frequent_subtree_sum(self):
        if self.dic_results:
            result = sorted(self.dic_results.items(), key=lambda x: x[1], reverse=True)
            max_f = result[0][1]
            return [_[0] for _ in result if _[1] == max_f]
        return []

    def subtree_sum(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root.left and not root.right:
            self.count(root.val)
            return root.val
        left, right = 0, 0
        if root.left:
            left = self.subtree_sum(root.left)
        if root.right:
            right = self.subtree_sum(root.right)
        sub_tree_sum = root.val + left + right
        self.count(sub_tree_sum)
        return sub_tree_sum

