#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
67. Add Binary

Given two binary strings, return their sum (also a binary string).
For example,
a = "11"
b = "1"
Return "100".
"""


def add_binary(a, b):
    """
        :type a: str
        :type b: str
        :rtype: str
    """
    if len(a) > len(b):
        a, b = b, a
    a = format(int(a), '0%dd' % len(b))
    r, c = [], 0
    for i in range(len(b), 0, -1):
        h = int(a[i-1]) + int(b[i-1]) + c
        r.append(str(h % 2))
        c = h // 2
    r.append(str(c))
    return ''.join(r[::-1])

if __name__ == '__main__':
    print(add_binary('1111', '10'))
