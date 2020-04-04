class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        first = True
        potential_sum = nums[0]
        max_sum = potential_sum
        for num in nums:
            if first:
                first = False
                continue
            if num >= potential_sum and potential_sum <= 0:
                potential_sum = num
            else:
                potential_sum += num
            max_sum = max(max_sum, potential_sum)
        return max_sum