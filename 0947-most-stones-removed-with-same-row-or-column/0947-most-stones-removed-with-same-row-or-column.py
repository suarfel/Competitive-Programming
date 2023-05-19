class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        
        rep = {i : i for i in range(len(stones))}
        
        rank = {i : 0 for i in range(len(stones))} 
        
        
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
            
            if rank[rootX] > rank[rootY]:
                rep[rootY] = rootX
            
            if rank[rootX] < rank[rootY]:
                rep[rootX] = rootY
            
            if rank[rootX] == rank[rootY]:
                rep[rootY] = rootX
                rank[rootX] += 1
        
        for i in range(len(stones)-1):
            for j in range(i+1,len(stones)):
                if stones[i][0] == stones[j][0] or stones[i][1] == stones[j][1]:
                    union(i,j)
        
        group_set = set()
        
        for i in range(len(stones)):
            group_set.add(find(i))
        
        return len(stones) - len(group_set)
            
            
            
        