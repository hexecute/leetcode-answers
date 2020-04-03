class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        seen = set()
        while (True):
            subtotal = 0
            while n > 0:
                mod = n % 10
                subtotal += mod * mod
                n = n / 10
            if subtotal == 1:
                return True
            elif subtotal in seen:
                return False
            else:
                seen.add(subtotal)
                n = subtotal