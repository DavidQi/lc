#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
647. Palindromic Substrings

Given a string, your task is to count how many palindromic substrings in this string.
The substrings with different start indexes or end indexes are counted as different substrings even they consist of
same characters.
Example 1:
Input: "abc"
Output: 3
Explanation: Three palindromic strings: "a", "b", "c".

Example 2:
Input: "aaa"
Output: 6
Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".

Note:
The input string length won't exceed 1000.
"""


def count_substrings(s):
    r, n = 0, len(s)
    for i in range(2*n - 1):
        left, right = i // 2, round(i/2)
        while left >= 0 and right < n and s[left] == s[right]:
            r += 1
            left -= 1
            right += 1
    return r

if __name__ == '__main__':
    print(count_substrings('aaa'))
