class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        
        rep = { i : i for i in range(1,n+1)}
        rank = {i:0 for i in range(1,n+1)}
      
        def find(x):
            
            root = x
            while root != rep[root]:
                root = rep[root]
            
            while x != root :
                parent = rep[x]
                rep[x] = root
                x = parent
                
            return root   
        
        def union(x,y):
            
            rootX = find(x)
            rootY = find(y)
            
            if rank[rootX] >  rank[rootY]:
                rep[rootY] = rootX
                
            if  rank[rootX] <  rank[rootY]:
                rep[rootX] = rootY
                
            if rank[rootX] ==  rank[rootY] :
                rep[rootY] = rootX
                rank[rootX] += 1
                
        min_dis = float('inf')     
        for road in roads: 
            union(road[0],road[1])
    
        for road in roads:
            if find(road[0]) == find(rep[1]):
                if min_dis > road[2]:
                    min_dis = road[2]
            if  find(road[1]) == find(rep[1]):
                if min_dis > road[2]:
                    min_dis = road[2] 
        return min_dis
                
            
            
        
      
            
        