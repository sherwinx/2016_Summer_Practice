import math
class Solution(object):
    def isPalindrome(self, x):
        if x < 0:
            return False
        if x == 0:
            return True
        digit = int(math.log(x,10)) + 1
        for i in range(digit/2):
            begin = x / (10 ** (digit - i - 1)) % 10
            end = (x / (10 ** i)) % 10
            if begin != end:
                return False
        return True
        
        """
        :type x: int
        :rtype: bool
        """
        