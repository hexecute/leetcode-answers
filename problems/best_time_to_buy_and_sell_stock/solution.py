class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        
        last_price = prices[0]
        is_profitable = False
        for price in prices:
            if price > last_price:
                is_profitable = True
        if not is_profitable:
            return 0
            
            
        Cases:
            Min before Max
            Max before Min
            All equal
        """
        if not prices:
            return 0
        
        buy_price = prices[0]
        max_profit = 0
        for price in prices:
            if price > buy_price:
                current_profit = price - buy_price
                max_profit = max(max_profit, current_profit)
            else:
                buy_price = price
        return max_profit
                
                
        