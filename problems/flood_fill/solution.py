class Solution(object):
    def floodFill(self, image, sr, sc, newColor):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type newColor: int
        :rtype: List[List[int]]
        """
        edited = []
        for _ in range(len(image)):
            edited.append([False] * len(image[0]))
        self.helper(image, edited, sc, sr, image[sr][sc], newColor)
        return image
    
    def helper(self, image, edited, x, y, oldColor, newColor):
        if (x >= len(image[0]) or x < 0):
            return
        if (y >= len(image) or y < 0):
            return
        if image[y][x] != oldColor or edited[y][x]:
            return
        image[y][x] = newColor
        edited[y][x] = True
        self.helper(image, edited, x - 1, y, oldColor, newColor)
        self.helper(image, edited, x + 1, y, oldColor, newColor)
        self.helper(image, edited, x, y - 1, oldColor, newColor)
        self.helper(image, edited, x, y + 1, oldColor, newColor)
    
    """
        height = len(image)
        width = len(image[0])
        rv = []
        
        for i in range(height):
            row = []
            for j in range(width):
                row.append(image[i][j])
            rv.append(row)

        return rv
    """
        