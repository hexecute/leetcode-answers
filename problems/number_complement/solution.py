from math import log

class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        if not num:
            return 1
        power = int(log(num, 2)) + 1
        return int(2 ** power - 1 - num)