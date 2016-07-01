class Solution(object):
    def isHappy(self, n):
        sumSet = set()
        while True:
            sum = 0
            while n:
                digit = n % 10
                sum += digit ** 2
                n /= 10
            if sum == 1:
                return True
            if sum in sumSet:
                return False
            sumSet.add(sum)
            n = sum
        """
        :type n: int
        :rtype: bool
        """
        