class Solution(object):
    def spiralOrder(self, matrix):
        if matrix == []:
            return []
        up = 0
        left = 0
        down = len(matrix) - 1
        right = len(matrix[0]) - 1
        direction = 0
        ans = []
        while True:
            #going right
            if direction == 0:
                for i in range(left, right + 1):
                    ans.append(matrix[up][i])
                up += 1
            if direction == 1:
                for i in range(up, down + 1):
                    ans.append(matrix[i][right])
                right -= 1
            if direction == 2:
                for i in range(right, left - 1, -1):
                    ans.append(matrix[down][i])
                down -= 1
            if direction == 3:
                for i in range(down, up - 1, -1):
                    ans.append(matrix[i][left])
                left += 1
            if up > down or left > right:
                return ans
            else:
                direction = (direction + 1) % 4
            
                
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """