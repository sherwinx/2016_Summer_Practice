class Solution(object):
    def generate(self, numRows):
        ans = []
        if numRows == 0:
            return ans
        prev_row = [1]
        ans.append(prev_row)
        for i in range(numRows - 1):
            new_row = [1]
            for j in range(len(prev_row) - 1):
                new_row.append(prev_row[j] + prev_row[j + 1])
            new_row.append(1)
            ans.append(new_row)
            prev_row = new_row
        
        return ans
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        