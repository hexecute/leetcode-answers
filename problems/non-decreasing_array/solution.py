class Solution(object):
    def checkPossibility(self, nums, exception=False):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums)
        for i in range(n - 1):
          if nums[i] > nums[i+1]:
              if exception:
                  return False
              else:
                  possibility_a = list(nums)
                  possibility_b = list(nums)
                  if (i == 0):
                    possibility_a[i] = -10001
                  else:
                    possibility_a[i] = possibility_a[i - 1]
                  possibility_b[i+1] = possibility_b[i]
                  return (self.checkPossibility(possibility_a, True) or self.checkPossibility(possibility_b, True))
        return True