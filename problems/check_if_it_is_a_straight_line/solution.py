class Solution(object):
    def checkStraightLine(self, coordinates):
        """
        :type coordinates: List[List[int]]
        :rtype: bool
        """
        # Calculate slope
        if (coordinates[1][0] - coordinates[0][0]):
            m = (coordinates[1][1] - coordinates[0][1]) / (coordinates[1][0] - coordinates[0][0])
        else:
            m = "v"
        for i in range(len(coordinates)):
            if not i:
                continue
            if (coordinates[i][0] - coordinates[i - 1][0]):
                slope = (coordinates[i][1] - coordinates[i - 1][1]) / (coordinates[i][0] - coordinates[i - 1][0])
            else:
                slope = "v"
            if slope != m:
                return False
        return True