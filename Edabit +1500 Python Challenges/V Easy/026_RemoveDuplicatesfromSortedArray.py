
class Solution(object):
    # def removeDuplicates(self, nums):
    #     """
    #         :type nums: List[int]
    #         :rtype: int
    #         """
    #     ls = len(nums)
    #     if ls <= 1:
    #         return ls
    #     last = nums[0]
    #     pos = 1
    #     for t in nums[1:]:
    #         if t == last:
    #             continue
    #         else:
    #             nums[pos] = t
    #             pos += 1
    #             last = t
    #     return pos

    # https://leetcode.com/articles/remove-duplicates-sorted-array/
    def removeDuplicates(self, nums):
        if len(nums) == 0:
            return 0
        left = 0
        for i in range(1, len(nums)):
            if nums[left] == nums[i]:
                continue
            else:
                left += 1
                nums[left] = nums[i]
        return left + 1



"""
Given a sorted array, remove the duplicates in place such that each element appear only once and return the new length.

Do not allocate extra space for another array, you must do this in place with constant memory.

For example,
Given input array A = [1,1,2],

Your function should return length = 2, and A is now [1,2].
"""
__author__ = 'Danyang'
class Solution:
    def removeDuplicates(self, A):
        """
        Algorithms: Two Pointers, open & closed
        Data structure: array
        Shifting the array

        del, pop(), or remove() are not allowed.
        return the length of "shrunk" array
        The array remains the same length

        :param A: list
        :return: "shrunk" list
        """
        length = len(A)

        # trivial
        if length==0 or length==1:
            return length

        # closed pointer, open pointer
        closed_ptr = 0
        open_ptr = 1
        while open_ptr<length:
            # find the next non-duplicate:
            if A[closed_ptr]==A[open_ptr]:
                open_ptr += 1
                continue  # go to the next iteration

            non_duplicate = A[open_ptr]
            A[closed_ptr+1] = non_duplicate
            closed_ptr += 1

        return closed_ptr+1 # length is index+1

    def removeDuplicates_another_loop_style(self, A):
        """
        Yet another looping style - double while loops
        :param A: list
        :return: "shrunk" list
        """
        length = len(A)

        if length==0 or length==1:
            return length

        closed_ptr = 0
        open_ptr = 1
        while open_ptr<length:
            while open_ptr<length and A[closed_ptr]==A[open_ptr]:
                open_ptr += 1

            if open_ptr<length:
                non_duplicate = A[open_ptr]
                A[closed_ptr+1] = non_duplicate
                closed_ptr += 1

        return closed_ptr+1 # length is index+1