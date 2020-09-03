# class Solution(object):
#     def intToRoman(self, num):
#         """
#         :type num: int
#         :rtype: str
#         """
#
class Solution(object):
    # def intToRoman(self, num):
    #     #http://www.rapidtables.com/convert/number/how-number-to-roman-numerals.htm
    #     roman_dim = [[1000, 'M'], [900, 'CM'], [500, 'D'], [400, 'CD'],
    #                  [100, 'C'], [90, 'XC'], [50, 'L'], [40, 'XL'], [10, 'X'],
    #                  [9,'IX'], [5, 'V'], [4, 'IV'], [1, 'I']]
    #     if num == 0:
    #         return ''
    #     roman_str = ''
    #     current, dim = num, 0
    #     while current != 0:
    #         while current // roman_dim[dim][0] == 0:
    #             dim += 1
    #         while current - roman_dim[dim][0] >= 0:
    #             current -= roman_dim[dim][0]
    #             roman_str += roman_dim[dim][1]
    #     return roman_str

    def intToRoman(self, num):
        values = [1000, 900, 500, 400,
                  100, 90, 50, 40,
                  10, 9, 5, 4, 1]
        symbols = ["M", "CM", "D", "CD",
                   "C", "XC", "L", "XL",
                   "X", "IX", "V", "IV",
                   "I"]
        roman = ''
        i = 0
        while num > 0:
            k = num / values[i]
            for j in range(k):
                roman += symbols[i]
                num -= values[i]
            i += 1
        return roman

if __name__ == '__main__':
    # begin
    s = Solution()
    print s.intToRoman(90)




"""
Given an integer, convert it to a roman numeral.

Input is guaranteed to be within the range from 1 to 3999.
"""

__author__ = 'Danyang'
int2roman = {
    1: "I",
    4: "IV",
    5: "V",
    9: "IX",

    10: "X",
    40: "XL",
    50: "L",
    90: "XC",

    100: "C",
    400: "CD",
    500: "D",
    900: "CM",

    1000: "M"
}


class Solution:
    def intToRoman(self, num):
        
        """
        dealing with digits
        notice the 1, 4, 5, 9, 10 repetition

        :param num: integer, Input is guaranteed to be within the range from 1 to 3999
        :return: a string
        """
        string_builder = []
        components = [1, 4, 5, 9, 10, 10, 40, 50, 90, 100, 400, 500, 900, 1000]

        # starting from the largest
        for component in reversed(components):  # reversed
            while num >= component:
                string_builder.append(int2roman[component])
                num -= component

        return "".join(string_builder)