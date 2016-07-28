import sys
import collections

#nums = [-1, -1, -1, 0, 0, 0, 1]
nums = [0,0,0]
target = 1 

def threeSum_closest(nums, target):
    ans = 0
    if len(nums) < 3:
        return ans
    nums.sort()
    minDiff = sys.maxint

    for i in range(len(nums) - 2):
        j = i + 1
        k = len(nums) - 1
        while j < k:
            threeSum = nums[i] + nums[j] + nums[k]
            offset = abs(target - threeSum)
            if target == threeSum:
                return target
            if offset < minDiff:
                minDiff = offset
                ans = threeSum 
            if threeSum > target:
                k -= 1
            else:
                j += 1

    return ans
print threeSum_closest(nums, target)
