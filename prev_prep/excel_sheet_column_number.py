class Solution(object):
    def titleToNumber(self, s):
        sol = 0
        length = len(s)
        for i in range(len(s)):
            sol += (26**(length - i - 1)) * (ord(s[i]) - ord('A') + 1) 
        return sol
        """
        :type s: str
        :rtype: int
        """
        