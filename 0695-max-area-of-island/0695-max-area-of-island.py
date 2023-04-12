class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        self.max_area = 0
        self.temp = []
        directions = [(1,0),(0,1),(0,-1),(-1,0)]
        visited = [[False for i in range(len(grid[0]))] for j in range(len(grid))]
        
        def in_bound(row,col):
            return 0 <= row < len(grid) and 0 <= col < len(grid[0])
        
        
        def dfs_grid(row,col,temp):
            
            visited[row][col] = True
            temp += 1
            
            for direction in directions:
                new_row = row + direction[0]
                new_col = col + direction[1]
                
                if in_bound(new_row,new_col) and not visited[new_row][new_col]:
                    if grid[new_row][new_col] == 1:
                        temp = dfs_grid(new_row,new_col,temp)
            return temp
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    temp = dfs_grid(i,j,0)
                    if temp > self.max_area:
                        self.max_area = temp
                        
        return self.max_area
                    
            
            
        