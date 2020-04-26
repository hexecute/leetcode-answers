class Solution(object):
    def __init__(self):
        self.helper_list = None
        
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) <= 1:
            return True

        furthest = 0
        for i in range(len(nums)):
            if i > furthest:
                return False
            elif furthest >= len(nums) - 1:
                return True
            furthest = max(i + nums[i], furthest)
    
    
    
        """
        Naive solution
        
        # Basic setup
        if self.helper_list == None:
            self.helper_list = [ False ] * len(nums)
            self.helper_list[0] = True
            
        if len(nums) <= 1:
            return True
        elif position >= len(nums):
            return False
        elif self.helper_list[position]:
            for i in range(nums[position]):
                new_position = position + i + 1
                if new_position >= len(nums):
                    break
                elif new_position == (len(nums) - 1):
                    return True
                self.helper_list[new_position] = True
        return self.canJump(nums, position + 1)
        """
            