#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
522. Longest Uncommon Subsequence II

Given a list of strings, you need to find the longest uncommon subsequence among them. The longest uncommon subsequence is defined as the longest subsequence of one of these strings and this subsequence should not be any subsequence of the other strings.
A subsequence is a sequence that can be derived from one sequence by deleting some characters without changing the order of the remaining elements. Trivially, any string is a subsequence of itself and an empty string is a subsequence of any string.
The input will be a list of strings, and the output needs to be the length of the longest uncommon subsequence. If the longest uncommon subsequence doesn't exist, return -1.
Example 1:
Input: "aba", "cdc", "eae"
Output: 3

Note:
All the given strings' lengths will not exceed 10.
The length of the given list will be in the range of [2, 50].
"""
from itertools import combinations


def longest_uncommon_substring_2(lst_s):
    """
        :type lst_s: List[str]
        :rtype: int
    """
    def get_longest_uncommon_substring(s_short, s_long):
        if s_short not in s_long:
            return s_long
        s1 = get_longest_uncommon_substring(s_long, s_short[:-1])
        s2 = get_longest_uncommon_substring(s_long, s_short[1:])
        if len(s1) > len(s2):
            return s1
        else:
            return s2

    r = []
    for a, b in combinations(lst_s, 2):
        if len(a) > len(b):
            a, b = b, a
        if len(a) == len(b):
            r.append(get_longest_uncommon_substring(b, a))
        r.append(get_longest_uncommon_substring(a, b))
    return len(set(r))

if __name__ == '__main__':
    print(longest_uncommon_substring_2(["aba", "cdc", "eae"]))
