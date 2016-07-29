from collections import *
import collections

#nums = [1, 0, -1, 0, -2, 2]
nums = [1,0,-1,0,-2,2]
target = 0
def fourSum(nums, target):
    table = collections.defaultdict(list)
    ans = []

    for i in range(len(nums)):
        table[nums[i]].append(i)

    pairTable = collections.defaultdict(list)
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            pairTable[(nums[i] + nums[j])].append((nums[i], nums[j]))  

    for twoSum in pairTable:
        cple = target - twoSum
        if cple in pairTable:
            for num, twoNum in pairTable[twoSum]:
                for threeNum, fourNum in pairTable[cple]:
                    ans.append([num, twoNum, threeNum, fourNum])
    ## Remove duplicates and sort each individual list
    for i in ans:
        i.sort()
    check = set() 
    for i in ans:
        if tuple(i) not in check:
            check.add(tuple(i))
    ret = []
    for i in check:
        ret.append(list(i))

    ans = list(ret)
    for eachAns in ret:
       listTable = dict(Counter(eachAns)) 
       for ele in listTable:
           if listTable[ele] > len(table[ele]):
               if eachAns in ans:
                   ans.remove(eachAns)
    return ans

print fourSum(nums, target)
