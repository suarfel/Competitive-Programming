class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        
        directions = [(0,1),(1,1),(-1,1),(1,0),(-1,-1),(1,-1),(-1,0),(0,-1)]
        
        def in_bound(row,col):
            return 0 <= row < len(grid) and 0 <= col < len(grid[0])
        
        def bfs(row,col,cost):
            if grid[0][0] != 0:
                return -1
            queue = deque([(row,col,cost+1)])
            visited = set([(row,col)]) 
            ans = []
            while queue:
               
                vertex = queue.popleft()
                ans.append(grid[vertex[0]][vertex[1]])
                
                for direction in directions:
                    
                    new_row = direction[0] + vertex[0]
                    new_col = direction[1] + vertex[1]
                    
                    if in_bound(new_row,new_col) and (new_row,new_col) not in visited:
                        if grid[new_row][new_col] == 0:
                            queue.append((new_row,new_col,vertex[2]+1))
                            visited.add((new_row,new_col))
                            if new_row == len(grid)-1 and new_col == len(grid[0])-1:
                                return queue[-1][-1]
            return -1
        if len(grid) == 1 and len(grid[0]) == 1 and grid[0][0] == 0:
            return 1
        return bfs(0,0,0)
                            
            
        