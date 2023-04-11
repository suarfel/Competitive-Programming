class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        directions = [(1,0),(0,1),(-1,0),(0,-1)]
        visited = [[False for i in range(len(grid[0]))] for j in range(len(grid))]
        def in_bound(row,col):
            return 0 <= row < len(grid) and 0 <= col < len(grid[0])
         
        
        def dfs_grid(row,col):
            
            visited[row][col] = True
            
            for direction in directions:
                new_row = row + direction[0]
                new_col = col + direction[1]
                
                if in_bound(new_row,new_col) and not visited[new_row][new_col]:
                    if grid[new_row][new_col] == "1":
                        dfs_grid(new_row,new_col)
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1" and not visited[i][j]:
                    dfs_grid(i,j)
                    count += 1
        return count
            
                
            
            
            
        