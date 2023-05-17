class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        
        graph = {1 : {'l','r'} , 2 : {'u','d'},3:{'u','l'},4:{'u','r'},5:{'d','l'},6:{'d','r'}}
        directions = [(1,0),(0,1),(0,-1),(-1,0)]
        rep = defaultdict(tuple)
        rank = defaultdict(int)

    
    
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                rep[(i,j)] = (i,j) 
                rank[(i,j)] = 0
                
        def in_bound(row,col):
            return (0 <= row < len(grid)) and ( 0 <= col < len(grid[0]))
        
        def find(x):
            
            root = x
            while root != rep[root]:
                root = rep[root] 
            while x != root:
                parent = rep[x]
                rep[x] = root
                x = parent
            return root 
        
        def union(x,y):
            
            rootX = find(x)
            rootY = find(y)
            
            if rootX != rootY:
                if rank[rootX] > rank[rootY]:
                    rep[rootY] = rootX
                if rank[rootY] > rank[rootX]:
                    rep[rootX] = rootY
                if rank[rootX] == rank[rootY]:
                    rep[rootY] = rootX
                    rank[rootX] += 1
                
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                
                # if rep[(i,j)] == (0,0):
                row = i
                col = j
                for dirc in directions:
                    new_row = row + dirc[0]
                    new_col = col + dirc[1]
                    if in_bound(new_row,new_col):
                        if new_row == row and new_col > col:
                            if 'r' in graph[grid[row][col]] and 'l' in graph[grid[new_row][new_col]]:
                                union((row,col),(new_row,new_col))
                        elif new_row == row and new_col < col:
                            if 'l' in graph[grid[row][col]] and 'r' in graph[grid[new_row][new_col]]:
                                union((row,col),(new_row,new_col))

                        elif new_col == col and new_row > row:
                            if 'u' in graph[grid[row][col]] and 'd' in graph[grid[new_row][new_col]]:
                                union((row,col),(new_row,new_col))
                        elif new_col == col and new_row < row:
                            if 'd' in graph[grid[row][col]] and 'u' in graph[grid[new_row][new_col]]: 
                                union((row,col),(new_row,new_col))
        # print(find((0,0))) 
        # print(find((len(grid)-1,len(grid[0])-1)))
        
        return find((0,0)) == find((len(grid)-1,len(grid[0])-1))



                
        
  
                    
                    
                
                
                                   
                