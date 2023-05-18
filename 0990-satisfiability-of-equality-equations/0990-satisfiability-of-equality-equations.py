class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        
        rep = {}
        for eq in equations:
            rep[eq[0]] = eq[0]
            rep[eq[3]] = eq[3]
        rank = {char : 0  for char in rep}
        
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
            
            if rank[rootX] > rank[rootY]:
                rep[rootY] = rootX 
            if rank[rootX] < rank[rootY]:
                rep[rootX] = rootY
            if rank[rootX] == rank[rootY]:
                rep[rootY] = rootX
        
        for eq in equations:
            
            if eq[1] == '=':
                union(eq[0],eq[3])
        
        for eq in equations:
            
            if eq[1] == '!':
                root1 = find(eq[0])
                root2 = find(eq[3])
                if root1 == root2:
                    return False
        return True
            
            
        