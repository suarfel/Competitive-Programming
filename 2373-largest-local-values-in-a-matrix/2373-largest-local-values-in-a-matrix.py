class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        
        
       
        matrix = []
        def find_max(start_row,start_col,final_row,final_col):
            max_val = 0
            temp_col = start_col
            while start_row <= final_row:
                while start_col <= final_col:
                    if grid[start_row][start_col] > max_val:
                        max_val = grid[start_row][start_col]
                    start_col += 1
                start_col = temp_col
                start_row += 1
            matrix[-1].append(max_val)
            
        i = j = 0
        while i < len(grid)-2:
            matrix.append([])
            while j < len(grid[0])-2:
                find_max(i,j,i+2,j+2)
                j += 1
            j = 0
            i += 1
            
        return matrix
                
                    
                    