import collections
#nums = [-1, 0, 1, 2, -1, -4]

nums = [-1, -1, -1, 0, 0, 0, 1]
def threeSum(nums):
    table = collections.defaultdict(list)
    ans = []
    for i in range(len(nums)):
        table[nums[i]].append(i)  
    # format {0:[1,2], 1:[3]}
    for num in table.keys():
        target = -num
        for twoNum in table.keys():
            if num == twoNum:
                if len(table[num]) == 1:
                    continue
            cple = target - twoNum
            if cple in table.keys():
                if cple == twoNum and twoNum == num:
                    if len(table[num]) < 3:
                        continue
                if cple == twoNum and len(table[twoNum]) == 1:
                    continue
                if cple == num and len(table[num]) == 1:
                    continue
                ans.append([num, twoNum,cple])
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
    return ret

def threeSum_v2(nums):
    ans = []
    if len(nums) < 3:
        return ans
    nums.sort()
    target = 0

    for i in range(len(nums) - 2):
        j = i + 1
        k = len(nums) - 1
        while j < k:
            if nums[i] + nums[j] + nums[k] > target:
                k -= 1
            elif nums[i] + nums[j] + nums[k] < target:
                j += 1
            else:
                ans.append([nums[i], nums[j], nums[k]])
                k -= 1
                j += 1
    
    check = set()
    for i in ans:
        if tuple(i) not in check:
            check.add(tuple(i))
    ret = []
    for i in check:
        ret.append(list(i))
    return ret

print threeSum(nums)
print threeSum_v2(nums)
