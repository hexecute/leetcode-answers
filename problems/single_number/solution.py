class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        helper = set()
        for num in nums:
            if num in helper:
                helper.remove(num)
            else:
                helper.add(num)
        return helper.pop()