class Solution(object):
    def countElements(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        helper_set = set(arr)
        count = 0
        for i in arr:
            if (i + 1) in helper_set:
                count += 1
        return count