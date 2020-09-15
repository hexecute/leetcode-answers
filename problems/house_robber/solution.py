class Solution(object):
    def __init__(self):
        self.foo = []
        """
        
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        return max(nums[0] + self.rob(nums[2:]), self.rob(nums[1:]))
        """
        
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        self.memory = [-1] * len(nums)
        self.nums_list = nums
        
        
        return self.rob_memoize(0)
    
    def rob_memoize(self, index):
        if index >= len(self.nums_list):
            return 0
        if self.memory[index] != -1:
            return self.memory[index]
        if index == (len(self.nums_list) - 1):
            self.memory[index] = self.nums_list[index]
            return self.memory[index]
        a = self.nums_list[index] + self.rob_memoize(index + 2)
        b = self.rob_memoize(index + 1)
        if (a >= b):
            self.memory[index] = a
        else:
            self.memory[index] = b
        return max(a, b)
        