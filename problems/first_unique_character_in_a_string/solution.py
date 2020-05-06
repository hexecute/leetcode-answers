

class Solution(object):
    def __init__(self):
        """
        """
        self.helper = {}

    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        for c in s:
            i = self.helper.get(c, 0)
            self.helper[c] = i + 1
        for i in range(len(s)):
            if self.helper[s[i]] == 1:
                return i
        return -1
        