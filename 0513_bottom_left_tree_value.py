#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
513. Find Bottom Left Tree Value

Given a binary tree, find the leftmost value in the last row of the tree.
Example 1:
Input:

    2
   / \
  1   3

Output:
1

Example 2:
Input:

        1
       / \
      2   3
     /   / \
    4   5   6
       /
      7

Output:
7

Note: You may assume the tree (i.e., the given root node) is not NULL.
"""


class BinaryTree(object):
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right


def bottom_left_tree_value(root):
    """
    :type root: TreeNode
    :rtype: int
    """
    levels = [root]
    for node in levels:
        levels += [_ for _ in (node.right, node.left) if _]
    return node.val

if __name__ == '__main__':
    tree = BinaryTree(1, BinaryTree(2, BinaryTree(4, )),
                      BinaryTree(3, BinaryTree(5, BinaryTree(7), BinaryTree(8)), BinaryTree(6)))
    print(bottom_left_tree_value(tree))
