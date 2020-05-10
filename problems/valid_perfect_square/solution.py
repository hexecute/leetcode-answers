class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num == 1:
            return True
        left = 1
        right = num - 1
        while right >= left:
            if right - left == 1:
                return False
            mid = int((left + right) / 2)
            potential = mid * mid
            if potential == num:
                return True
            elif potential < num:
                left = mid
            elif potential > num:
                right = mid
        return False
        
        """
        potential = num ** 0.5
        if (potential == int(potential)):
            return True
        return False
        """