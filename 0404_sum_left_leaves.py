#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
404. Sum of Left Leaves

Find the sum of all left leaves in a given binary tree.
Example:
    3
   / \
  9  20
    /  \
   15   7

There are two left leaves in the binary tree, with values 9 and 15 respectively. Return 24.
"""


class BinaryTree(object):
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right


def sum_left_leavres(root):
    """
        :type root: TreeNode
        :rtype: int
    """
    return sum_left_leavres(root.left) + sum_left_leavres(root.right) + root.left.val if root and root.left else 0


if __name__ == '__main__':
    tree = BinaryTree(1, BinaryTree(2, BinaryTree(4, )),
                      BinaryTree(3, BinaryTree(5, BinaryTree(7), BinaryTree(8)), BinaryTree(6)))
    print(sum_left_leavres(tree))

