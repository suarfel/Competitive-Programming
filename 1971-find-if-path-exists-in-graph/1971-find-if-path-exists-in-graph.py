class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        
        representative = {i : i for i in range(n)}
        rank = [0 for i in range(n)]
        
        def find_rep(x):
            
            root = x 
            while root != representative[root]:
                root = representative[root]
                
            while x != root:
                parent = representative[x]
                representative[x] = root
                x = parent
                
            return root
        
        def union(x,y):
            
            rootX = find_rep(x)
            rootY = find_rep(y)
            if rootX != rootY:
                
                if rank[rootX] > rank[rootY]:
                    representative[rootY] = rootX
                if rank[rootX] < rank[rootY]:
                    representative[rootX] = rootY
                if rank[rootX] == rank[rootY]:
                    representative[rootY] = rootX
                    rank[rootX] += 1
                   
        
        for edge in edges:
            union(edge[0],edge[1])
          
        return find_rep(source) == find_rep(destination)
            
            
        
        
        