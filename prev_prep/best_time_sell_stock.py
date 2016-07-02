class Solution(object):
    def maxProfit(self, prices):
        min = float("inf")
        maxProfit = 0
        for price in prices:
            if price <= min:
                min = price
            if maxProfit < price - min:
                maxProfit = price - min
        return maxProfit
        """
        :type prices: List[int]
        :rtype: int
        """
        