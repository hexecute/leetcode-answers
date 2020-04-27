# """
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# """
#class BinaryMatrix(object):
#    def get(self, x, y):
#        """
#        :type x : int, y : int
#        :rtype int
#        """
#
#    def dimensions:
#        """
#        :rtype list[]
#        """

class Solution(object):
    def leftMostColumnWithOne(self, binaryMatrix):
        """
        :type binaryMatrix: BinaryMatrix
        :rtype: int
        """
        self.binaryMatrix = binaryMatrix
        self.height, self.width = binaryMatrix.dimensions()
        rv = self.width
        for i in range(self.height):
            if rv == self.width:
                furthest_to_search = rv - 1
            else:
                furthest_to_search = rv
            rv = min(rv, self.binarySearch(0, furthest_to_search, i))
        if rv == self.width:
            return -1
        return rv
    
    def binarySearch(self, min_x, max_x, y):
        if (max_x - min_x) <= 1:
            left = self.binaryMatrix.get(y, min_x)
            right = self.binaryMatrix.get(y, max_x)
            if left == 1:
                return min_x
            elif right == 1:
                return max_x
            else:
                return self.width
        mid_x = (min_x + max_x) / 2
        if self.binaryMatrix.get(y, mid_x):
            return self.binarySearch(min_x, mid_x, y)
        else:
            return self.binarySearch(mid_x, max_x, y)