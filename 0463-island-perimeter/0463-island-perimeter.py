class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        self.count = 0
        directions = [(0,1),(1,0),(-1,0),(0,-1)]
        visited = [[False for i in range(len(grid[0]))] for j in range(len(grid))]
        print(visited)
        def in_bound(row,col):
            return 0 <= row < len(grid) and 0 <= col < len(grid[0])
        
        def dfs_grid(row,col):
            
            visited[row][col] = True
            for direction in directions:
                new_row = row + direction[0]
                new_col = col + direction[1]
                if not in_bound(new_row,new_col) and grid[row][col]:
                    self.count += 1
                if not grid[row][col] and in_bound(new_row,new_col) and grid[new_row][new_col]:
                    self.count += 1
                if in_bound(new_row,new_col) and not visited[new_row][new_col]:
                    dfs_grid(new_row,new_col)
        dfs_grid(0,0)
        return self.count
                    
            
        
                
        