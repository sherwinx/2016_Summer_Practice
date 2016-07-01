class Solution(object):
    def rob(self, nums):
        if nums == []:
            return 0
        if len(nums) == 1:
            return nums[0]
        maxProf = [0] * (len(nums) + 1)
        maxProf[0] = 0
        maxProf[1] = nums[0]
        for i in range(2,len(maxProf)):
            maxProf[i] = max(maxProf[i-1], maxProf[i-2] + nums[i-1])
        return maxProf[-1]
            
        
        """
        Dynamic Programming
        :type nums: List[int]
        :rtype: int
        """
        

