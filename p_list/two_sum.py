import collections
nums = [0,4,3,0] 
target = 0

def twoSum(nums, target):
    table = collections.defaultdict(list)
    ans = []
    for i in range(len(nums)):
        table[nums[i]].append(i)  
    # format {0:[1,2], 1:[3]}
    for num in table.keys():
        cple = target - num
        if cple in table:
            if cple == num:
                if len(table[num]) == 1:
                    continue
                else:
                    ans.append(table[num][0])
                    ans.append(table[num][1])
                    return ans 
            else:
                ans.append(table[num][0])
                ans.append(table[cple][0])
                return ans 
        
print twoSum(nums, target)
