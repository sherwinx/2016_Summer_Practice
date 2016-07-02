class Solution(object):
    def plusOne(self, digits):
        if digits == []:
            return [1]
        original_length = len(digits)
        length = len(digits) - 1
        while True:
            digits[length] += 1
            if digits[length] != 10:
                break
            digits[length] = 0
            length -= 1
            if length < 0:
                new_list = [1]
                return new_list + [0] * original_length
        
        return digits
            
            
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        