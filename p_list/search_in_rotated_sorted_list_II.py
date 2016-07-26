myList = [1,3,1,1,1]
def searchRotated(num, myList):
    start = 0
    end = len(myList) - 1
    while start != end and end >= 0 and start >= 0:  
        ##whether it's monotonically increse, no matter the whole thing is rotated or not
        mid = (start + end) / 2
        if num == myList[mid]:
            return True
        if myList[mid] > myList[start]:
            if myList[mid] >= num and num >= myList[start]:
                end = mid
            else:
                start = mid + 1
        elif myList[mid] < myList[start]:
             if myList[mid] < num and num <= myList[end]:
                 start = mid + 1
             else:
                 end = mid
        else:
            start = start + 1
    if myList[start] == num:
        return True 
    else:
        return False 

print searchRotated(5, myList)

