import math

class Solution(object):
    def trailingZeroes(self, n):
        x = 5
        ans = 0
        while x <= n:
            ans += n / x
            x *= 5
        return ans
        
        """
        :type n: int
        :rtype: int
        """
        