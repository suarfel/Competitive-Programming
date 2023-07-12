class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        
        
        def total_check(row,col):
            first_checker = set()
            second_checker = set()
            
            for i in range(row,row+3):
                row_sum = 0
                for j in range(col,col+3):
                    row_sum += grid[i][j]
                    if  0 < grid[i][j] and grid[i][j] < 10:
                        second_checker.add(grid[i][j])
                first_checker.add(row_sum)
                
            
            for i in range(col,col+3):
                col_sum = 0
                for j in range(row,row+3):
                    col_sum += grid[j][i]
                first_checker.add(col_sum)
                
            first_diag_sum = grid[row][col] + grid[row+1][col+1] + grid[row+2][col+2]  
            second_diat_sum = grid[row][col+2] + grid[row+1][col+1] + grid[row+2][col] 
            first_checker.add(first_diag_sum)
            first_checker.add(second_diat_sum)
            
            return len(first_checker) == 1 and len(second_checker) == 9
        
        if len(grid) < 3 or len(grid[0]) < 3:
            return 0
        
        count = 0
        for i in range(len(grid)-2):
            for j in range(len(grid[0])-2):
                if total_check(i,j):
                    count += 1
                    
        return count
                
                
        
        