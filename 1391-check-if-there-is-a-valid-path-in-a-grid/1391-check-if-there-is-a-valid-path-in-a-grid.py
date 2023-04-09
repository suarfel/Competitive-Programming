class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        
        graph =  {}
        
        graph = {1 : {'l','r'} , 2 : {'u','d'},3:{'u','l'},4:{'u','r'},5:{'d','l'},6:{'d','r'}}
        
        directions = [(1,0),(0,1),(0,-1),(-1,0)]
        visited = [[False for j in range(len(grid[0]))] for i in range(len(grid))]
      
        def in_bound(row,col):
            return (0 <= row < len(grid)) and (0 <= col < len(grid[0]))
        
        def dfs_grid(row,col):
            
            if row == len(grid) - 1 and col == len(grid[0]) - 1:
                return True
            visited[row][col] = True
            
            for direction in directions:
                new_row = row + direction[0]
                new_col = col + direction[1]
                if in_bound(new_row,new_col) and not visited[new_row][new_col]:
                    if new_row == row and new_col > col:
                        if 'r' in graph[grid[row][col]] and 'l' in graph[grid[new_row][new_col]]:
                            r = dfs_grid(new_row,new_col)
                            if r:
                                return True
                    elif new_row == row and new_col < col:
                        if 'l' in graph[grid[row][col]] and 'r' in graph[grid[new_row][new_col]]:
                            r = dfs_grid(new_row,new_col)
                            if r:
                                return True
                    elif new_col == col and new_row > row:
                        if 'u' in graph[grid[row][col]] and 'd' in graph[grid[new_row][new_col]]:
                            r = dfs_grid(new_row,new_col)
                            if r:
                                return True
                    elif new_col == col and new_row < row:
                        if 'd' in graph[grid[row][col]] and 'u' in graph[grid[new_row][new_col]]: 
                            r = dfs_grid(new_row,new_col)
                            if r:
                                return True
            return False
        return dfs_grid(0,0)
            
            
            
                    
                    
                
                
                                   
                