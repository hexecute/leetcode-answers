class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        target = len(nums) / 2
        helper = {}
        for num in nums:
            temp = helper.get(num, 0) + 1
            if temp > target:
                return num
            helper[num] = temp
        return -1
            
        