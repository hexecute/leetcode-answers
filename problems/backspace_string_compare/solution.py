class Solution(object):
    def backspaceCompare(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """
        helper_1 = []
        helper_2 = []
        for char in S:
            if char == "#":
                if helper_1:
                    helper_1.pop()
            else:
                helper_1.append(char)
        for char in T:
            if char == "#":
                if helper_2:
                    helper_2.pop()
            else:
                helper_2.append(char)
        return helper_1 == helper_2
        
        