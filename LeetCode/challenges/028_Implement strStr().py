"""
Implement strStr().

Returns a pointer to the first occurrence of needle in haystack, or null if needle is not part of haystack.
"""
__author__ = 'Danyang'
class Solution:
    def strStr_brute_force(self, haystack, needle):
        """
        Algorithm:
        two pointers

        :param haystack: str
        :param needle: str
        :return: str or None
        """
        l_hay = len(haystack)
        l_ndl = len(needle)
        for i in xrange(l_hay-l_ndl+1):  # i+l_ndl <= l_hay
            if haystack[i:i+l_ndl]==needle:
                return haystack[i:]
        return None

    def strStr(self, haystack, needle):
        """
        KMP algorithm
        :type haystack: str
        :type needle: str
        :param haystack:
        :param needle:
        :return:
        """
        ln = len(needle)
        lh = len(haystack)
        if ln==0:
            return haystack
        if ln==1:
            try:
                index = haystack.index(needle)
                return haystack[index:]
            except ValueError:
                return None

        # construct T
        T = [0 for _ in xrange(ln)]
        T[0] = -1
        T[1] = 0
        pos = 2
        cnd = 0
        while pos<ln:
            if needle[pos-1]==needle[cnd]:  # pos-1 rather than pos
                cnd += 1
                T[pos] = cnd
                pos += 1
            elif T[cnd]!=-1:
                cnd = T[cnd]
            else:
                cnd = 0
                T[pos] = cnd
                pos += 1

        # search
        i = 0
        m = 0
        while m+i<lh:
            if needle[i]==haystack[m+i]:
                i += 1
                if i==ln:
                    return haystack[m:]
            else:
                if T[i]!=-1:
                    m = m+i-T[i]
                    i = T[i]
                else:
                    m += 1
                    i = 0

        return None


if __name__=="__main__":
    needle = "ABCDABD"
    haystack = "ABC ABCDAB ABCDABCDABDE"
    needle = "aaa"
    haystack = "aaa"
    solution = Solution()
    assert solution.strStr_brute_force(haystack, needle)==solution.strStr(haystack, needle)





class Solution(object):
    # def strStr(self, haystack, needle):
    #     """
    #     :type haystack: str
    #     :type needle: str
    #     :rtype: int
    #     """
    #     lsh, lsn = len(haystack), len(needle)
    #     if lsn == 0:
    #         return 0
    #     pos, index = 0, 0
    #     while index <= lsh - lsn:
    #         if haystack[index] == needle[pos]:
    #             backup = index
    #             while index < lsh and pos < lsn and haystack[index] == needle[pos]:
    #                 pos += 1
    #                 index += 1
    #             if pos == len(needle):
    #                 return index - pos
    #             index = backup
    #         index += 1
    #         pos = 0
    #     return -1

    # def strStr(self, haystack, needle):
    #     lsh, lsn = len(haystack), len(needle)
    #     if lsn == 0:
    #         return 0
    #     pos, index = 0, 0
    #     while index <= lsh - lsn:
    #         if haystack[index] == needle[0]:
    #             # slice index:index + lsn
    #             if haystack[index:index + lsn] == needle:
    #                 return index
    #         index += 1
    #     return -1

    # KMP
    # https://discuss.leetcode.com/topic/3576/accepted-kmp-solution-in-java-for-reference/2
    def strStr(self, haystack, needle):
        lsh, lsn = len(haystack), len(needle)
        if lsn == 0:
            return 0
        next = self.makeNext(needle)
        i = j = 0
        while i < lsh:
            if j == -1 or haystack[i] == needle[j]:
                i += 1
                j += 1
                if j == lsn:
                    return i - lsn
            if i < lsh and haystack[i] != needle[j]:
                j = next[j]
        return -1

    def makeNext(self, needle):
        ls = len(needle)
        next = [0] * ls
        next[0], i, j = -1, 0, -1
        while i < ls - 1:
            if j == -1 or needle[i] == needle[j]:
                next[i + 1] = j + 1
                if needle[i + 1] == needle[j + 1]:
                    next[i + 1] = next[j + 1]
                i += 1
                j += 1
            if needle[i] != needle[j]:
                j = next[j]
        return next

