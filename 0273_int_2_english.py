#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
273. Integer to English Words

Convert a non-negative integer to its english words representation. Given input is guaranteed to be less than 231 - 1.
For example,
123 -> "One Hundred Twenty Three"
12345 -> "Twelve Thousand Three Hundred Forty Five"
1234567 -> "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"
"""


def int_2_english(num):
    """
    :type num: int
    :rtype: str
    """
    dic_mapping = {1: 'One', 2: 'Two', 3: 'Three', 4: 'Four', 5: 'Five', 6: 'Six', 7: 'Seven', 8: 'Eight', 9: 'Nine',
                   10: 'Ten', 11: 'Eleven', 12: 'Twelve', 13: 'Thirteen', 14: 'Fourteen', 15: 'Fifteen', 16: 'Sixteen',
                   17: 'Seventeen', 18: 'Eighteen', 19: 'Nineteen', 20: 'Twenty', 30: 'Thirty', 40: 'Fourty',
                   50: 'Fifty', 60: 'Sixty', 70: 'Seventy', 80: 'Eight', 90: 'Ninety'}
    lst_units = ['Thousand', 'Million', 'Billion', 'Trillion']

    def translate(n):
        if n == 0:
            return []
        elif n < 20:
            return [dic_mapping[n]]
        elif n < 100:
            return [dic_mapping.get(n) or dic_mapping[n//10*10]] + translate(n % 10)
        elif n < 1000:
            return [dic_mapping[n//100]] + ['Hundred'] + translate(n % 100)
        else:
            for i, w in enumerate(lst_units, 1):
                if n < 1000 ** (i+1):
                    return translate(n//1000 ** i) + [w] + translate(n % 1000 ** i)
    return ' '.join(translate(num))

if __name__ == '__main__':
    print(int_2_english(1550200000))
