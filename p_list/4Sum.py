import collections

#nums = [1, 0, -1, 0, -2, 2]
nums = [1,0,-1,0,-2,2]
target = 0
def threeSum(nums, target):
    table = collections.defaultdict(list)
    ans = []
    for i in range(len(nums)):
        table[nums[i]].append(i)  
    # format {0:[1,2], 1:[3]}

    for num in table.keys():
        rest = target - num
        for twoNum in table.keys():
            if num == twoNum and len(table[num]) == 1:
                continue
            cple = rest - twoNum
            for threeNum in table.keys(): 
                if threeNum == twoNum and twoNum == num and len(table[num]) < 3:
                    continue
                if threeNum  == twoNum and len(table[twoNum]) == 1:
                    continue
                if threeNum == num and len(table[num]) == 1:
                    continue
                last = cple - threeNum
                if last in table.keys():
                    if last == num and len(table[last]) == 1:
                        continue
                    if last == twoNum and len(table[last]) == 1:
                        continue
                    if last == threeNum and len(table[last]) == 1:
                        continue
                    if last == num and last == twoNum and len(table[last]) < 3:
                        continue 
                    if last == num and last == threeNum and len(table[last]) < 3:
                        continue 
                    if last == twoNum and last == threeNum and len(table[last]) < 3:
                        continue 
                    if last == twoNum and last == threeNum and last == num and len(table[last]) < 4:
                        continue
                    else:
                        ans.append([num, twoNum, threeNum, last])
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

print threeSum(nums, target)
