class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        def char_to_int(char):
            return ord(char) - 97
        
        s_array = [0] * 26
        t_array = [0] * 26

        for c in s:
            s_array[char_to_int(c)] += 1
        for c in t:
            t_array[char_to_int(c)] += 1
        for i in range(26):
            if s_array[i] != t_array[i]:
                return chr(i + 97)
        
        