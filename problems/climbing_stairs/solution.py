class Solution(object):

    def __init__(self):
        self.memory = [ -1 ] * 46
        self.memory[1] = 1
        self.memory[2] = 2
    
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """

        if n == 1:
            return 1
        if n == 2:
            return 2
        
        if self.memory[n - 1] != -1:
            left = self.memory[n - 1]
        else:
            left = self.climbStairs(n - 1)
            self.memory[n - 1] = left
            
            
        if self.memory[n - 2] != -1:
            right = self.memory[n - 2]
        else:
            right = self.climbStairs(n - 2)
            self.memory[n - 2] = right
            
        return left + right