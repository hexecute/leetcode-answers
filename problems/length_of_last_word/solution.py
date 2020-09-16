class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        arr = s.strip().split(" ")
        return len(arr[-1])