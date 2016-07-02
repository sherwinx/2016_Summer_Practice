class Solution(object):
    def hammingWeight(self, n):
        ans = 0
        while n:
            n = n & (n-1)
            ans += 1
        return ans
        """
        :type n: int
        :rtype: int
        """
        