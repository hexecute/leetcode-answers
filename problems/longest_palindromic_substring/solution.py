class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s:
            return ""
        self.rv = s[0]
        self.rv_length = 1
        
        self.length = len(s)
        for i in range(self.length):
            # Assume that s[i] is center of palindrome
            self.f(s, i, i)
            
            self.f(s, i + 1, i)
        return self.rv
    
    def f(self, s, left, right):
        while True:
            left -= 1
            right += 1
            if left < 0 or right >= self.length:
                return
            if s[left] == s[right]:
                if (right - left + 1) > self.rv_length:
                    potential = s[left:right + 1]
                    potential_length = len(potential)
                    if potential_length > self.rv_length:
                        self.rv = potential
                        self.rv_length = potential_length
            else:
                return
    
