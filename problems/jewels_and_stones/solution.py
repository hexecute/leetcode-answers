class Solution(object):
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        jewel_set = set()
        jewel_num = 0
        for jewel in J:
            jewel_set.add(jewel)
        for stone in S:
            if stone in jewel_set:
                jewel_num += 1
        return jewel_num
            