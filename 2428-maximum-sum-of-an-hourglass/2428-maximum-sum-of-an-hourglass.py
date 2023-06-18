class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        
        i=j = 0
        max_sum = 0
        while i < len(grid)-2:
            while j < len(grid[0])-2:
                temp_sum = grid[i][j] + grid[i][j+1] + grid[i][j+2] + grid[i+1][j+1] + grid[i+2][j] + grid[i+2][j+1] + grid[i+2][j+2]
                if temp_sum > max_sum:
                    max_sum = temp_sum
                j += 1
            j = 0
            i += 1

        return max_sum
                
                
                
        