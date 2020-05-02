# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        left = 1
        right = n
        while (True):
            if right - left <= 1:
                if isBadVersion(left):
                    return left
                else:
                    return right
            target = (left + right) / 2
            if not isBadVersion(target):
                left = target + 1
                continue
            else:
                right = target 
                continue
            
            
        