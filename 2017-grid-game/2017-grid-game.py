class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        
        matrix = [[0]*len(grid[0]) for i in range(len(grid))]
        total = 0
        
        for i in range(len(grid)):
            matrix[i][0] = grid[i][0]
            total += grid[i][0]
            for j in range(1,len(grid[0])):
                matrix[i][j] = grid[i][j] + matrix[i][j-1]
                total += grid[i][j]
        
        ans = float('inf')
        temp = float('inf')
        
        for i in range(len(grid[0])):
            if i == 0:
                ans = matrix[0][-1] - matrix[0][i]
            else:
                temp = max(matrix[0][-1] - matrix[0][i], matrix[1][i-1])
            
            ans = min(ans,temp)
        
        return ans
        
        
            
            
                
                
             