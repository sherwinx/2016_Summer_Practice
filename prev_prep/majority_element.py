import collections
import math
class Solution(object):
    def majorityElement(self, nums):
        candidate, count = None, 0
        for num in nums:
            if count == 0:
                candidate, count = num, 1
            elif num == candidate:
                count += 1
            else:
                count -= 1
        if count <= 0:
            return None
        else:
            check = 0
            for i in nums:
                if i == candidate:
                    check += 1
            if check > len(nums) / 2:
                return candidate
            else:
                return None

"""    def majorityElement(self, nums):
        length = len(nums)
        numDict = collections.defaultdict(lambda:0)
        for i in nums:
            numDict[i] += 1
            if numDict[i] >= length / math.ceil(2):
                return i
        return 0

门罗投票算法 时间O(n) 空间 O（1）
Algorithm 3: Boyer-Moore Vote Algorithm
Step 1: Find a candidate for majority element.
Step 2: Check if this candidate is a majority element.
Step1:
Find the candidate for majority element
1: Initialize count of current candidate as 0, count = 0
2: Iterate over the array and do following steps:
(a) If count == 0, set candidate = array[i], count = 1
(b) Else (i) If candidate == array[i], set count = count + 1 (ii) else set count = count - 1
Step 2: 
Check if candidate is Majority Element
1: If count == 0, there is no majority element.
2: Else, iterate over array to get count of candidate. (a) If count is greater than n/2, return candidate (b) Else return null;

"""