class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        
        directions = [(0,1),(1,0),(-1,0),(0,-1)]
        
        visited = [[False for i in range(len(image[0]))] for j in range(len(image))]
        
        
        def in_bound(row,col):
            return 0 <= row < len(image) and 0 <= col < len(image[0])
        
        val = image[sr][sc]
        
        def dfs_grid(row,col):
            
            visited[row][col] = True
            image[row][col] = color
            
            for direction in directions:
                new_row = row + direction[0]
                new_col = col + direction[1]
                
                if in_bound(new_row,new_col) and not visited[new_row][new_col]:
                    if image[new_row][new_col] == val:
                        dfs_grid(new_row,new_col)
        dfs_grid(sr,sc)
        return image
                    
        