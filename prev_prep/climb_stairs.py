class Solution(object):
    def climbStairs(self, n):
        if n == 0:
            return 0
        a = b = 1
        for i in range(2, n + 1):
            a, b = b, a + b
        return b
        
        """
        :type n: int
        :rtype: int
        """