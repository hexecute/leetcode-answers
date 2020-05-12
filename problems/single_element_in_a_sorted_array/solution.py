class Solution(object):
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left = 0
        right = len(nums) - 1
        if not right:
            return nums[0]
        while (True):
            if (right - left > 2):
                mid = (left + right) / 2
                if (nums[mid - 1] == nums[mid]):
                    if (right - mid) % 2 == 0:
                        right = mid - 2
                    else:
                        left = mid + 1
                elif (nums[mid] == nums[mid + 1]):
                    if (mid - left) % 2 == 0:
                        left = mid + 2
                    else:
                        right = mid - 1
                else:
                    return nums[mid]
            elif right - left >= 1: # right - left == 2
                if (nums[left] == nums[left + 1]):
                    return nums[right]
                else:
                    return nums[left]
            else:
                return nums[left] # nums[right]