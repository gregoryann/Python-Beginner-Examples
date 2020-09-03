"""
Given a roman numeral, convert it to an integer.

Input is guaranteed to be within the range from 1 to 3999.
"""
__author__ = 'Danyang'
roman2int = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000
}


class Solution:
    def romanToInt(self, s):
        """
        What happens if current roman char larger than the previous roman char?

        :param s: String
        :return: integer
        """
        result = 0
        for ind, val in enumerate(s):
            if ind > 0 and roman2int[val] > roman2int[s[ind-1]]:  # e.g. XIV
                result -= roman2int[s[ind-1]]  # reverse last action
                result += roman2int[val]-roman2int[s[ind-1]]
            else:
                result += roman2int[val]

        return result




class Solution:
    # def romanToInt(self, s):
    #     """
    #     :type s: str
    #     :rtype: int
    #     """
    #     roman = {'I': 1, 'V': 5, 'X': 10,
    #              'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    #     result = 0
    #     last = s[-1]
    #     for t in reversed(s):
    #         if t == 'C' and last in ['D', 'M']:
    #             result -= roman[t]
    #         elif t == 'X' and last in ['L', 'C']:
    #             result -= roman[t]
    #         elif t == 'I' and last in ['V', 'X']:
    #             result -= roman[t]
    #         else:
    #             result += roman[t]
    #         last = t
    #     return result

    def romanToInt(self, s):
        roman = {'I': 1, 'V': 5, 'X': 10,
                 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        prev, total = 0, 0
        for c in s:
            curr = roman[c]
            total += curr
            # need to subtract
            if curr > prev:
                total -= 2 * prev
            prev = curr
        return total


