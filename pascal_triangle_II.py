class Solution(object):
    def getRow(self, rowIndex):
        curr_row = [1]
        for j in range(rowIndex):
            prev_row = curr_row                    
            curr_row = [1]
            for i in range(len(prev_row) - 1):
                curr_row.append(prev_row[i] + prev_row[i+1])
            curr_row.append(1)
        return curr_row
        
        
        
        
    
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        