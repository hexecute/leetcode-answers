class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        i = 0
        end = len(nums)
        while (i < end):
            if not nums[i]:
                del nums[i]
                nums.append(0)
                end -= 1
            else:
                i += 1
        