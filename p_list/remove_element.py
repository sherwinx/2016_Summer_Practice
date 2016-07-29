nums = [2,2]
val = 2 


def removeElement(nums, val):
   start = 0
  
   for i in range(len(nums)):
       if nums[i] != val:
           nums[start] = nums[i]
           start += 1
   print nums[:start]
   return start

           

print removeElement(nums, val)
