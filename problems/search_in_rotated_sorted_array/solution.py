class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums:
            return -1
        start = nums[0]
        end = nums[-1]
        mid = nums[len(nums)/2]
        
        print(nums)

        # Base cases
        if target == start:
            return 0
        elif target == end:
            return len(nums) - 1
        elif target == mid:
            return len(nums)/2
        elif start == end:
            return -1
        
        if (mid > start and target > start and target < mid) or \
           (mid > start and target < start and target > mid) or \
           (mid < start and target < start and target < mid) or \
           (mid < start and target > start and target > mid):
            return self.search(nums[:len(nums)/2], target)
        else:
            temp = self.search(nums[len(nums)/2:], target)
            if temp == -1:
                return -1
            else:
                return temp + len(nums)/2