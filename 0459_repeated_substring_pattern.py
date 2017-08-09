#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
459. Repeated Substring Pattern

Given a non-empty string check if it can be constructed by taking a substring of it and appending multiple copies of
the substring together. You may assume the given string consists of lowercase English letters only and its length will
not exceed 10000.

Example 1:
Input: "abab"

Output: True

Explanation: It's the substring "ab" twice.

Example 2:
Input: "aba"

Output: False

Example 3:
Input: "abcabcabcabc"

Output: True

Explanation: It's the substring "abc" four times. (And the substring "abcabc" twice.)
"""


def get_factors(n):
    r = []
    for i in range(2, int(n**0.5)+1):  # not include 1 and itself, int(n**0.5) 表示不大于n的平方根的最大整数
        if n % i == 0 and i not in r:
            r.append(i)
            x = n // i
            r.append(x) if x not in r else 0
    return r


class Solution(object):
    """
    思路：
    如果一个字串内是否由一个更短的字串重复n次而构成，
    那么子字串的长度必然为字串长度的约数。
    所以得到字串长度的所有约数，
    然后按照约数获取各个子字串并比较
    """
    def __init__(self, s):
        self.s = s

    def get_substring(self):
        r, k = [], len(self.s)
        for i in get_factors(k):
            l = [self.s[j:j+i] for j in range(0, k, i)]
            r.append(l[0]) if len(set(l)) == 1 else 0
        return r

    def repeated_substring_pattern(self):
        """
            :type s: str
            :rtype: bool
        """
        k = len(self.s)
        for i in get_factors(k):
            ss = ''
            for j in range(0, k, i):
                if ss == '':
                    ss = self.s[j:j+i]
                    continue
                if ss != self.s[j:j+i] :
                    ss = ''
                    break
            if ss:
                return True
        return False

if __name__ == '__main__':
    s = ['testtest', 'bcdbcdbcde', 'testedtested', 'aaaaaaaaaa']
    for i in s:
        o = Solution(i)
        print(o.get_substring())
        print(o.repeated_substring_pattern())
