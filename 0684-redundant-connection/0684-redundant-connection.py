class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        
        representative = {i+1 : i+1 for i in range(len(edges))}
        rank = [0 for i in range(len(edges)+1)]
        
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
                   
        ans = []
        for edge in edges:
            
            if find_rep(edge[0]) == find_rep(edge[1]):
                ans = edge
            union(edge[0],edge[1])
        
        return ans
            