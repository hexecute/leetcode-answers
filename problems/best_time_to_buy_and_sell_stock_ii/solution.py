class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        total = 0
        if prices:
            bought = prices[0]
        # Always increasing?
        for price in prices:
            if price > bought:
                total += price - bought
            bought = price
        return total