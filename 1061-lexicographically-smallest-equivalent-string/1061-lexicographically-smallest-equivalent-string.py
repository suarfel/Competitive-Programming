class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        long_string = s1 + s2 + baseStr
        rep = {char : char for char in long_string}
        
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
            
            if rootX < rootY:
                rep[rootY] = rootX
            if rootX > rootY:
                rep[rootX] = rootY
            if rootY == rootX:
                rep[rootX] = rootY
                
        for i in range(len(s1)):
            union(s1[i],s2[i])
        st = ''
        for char in baseStr:
            st += find(char)
            
        return st
            
        
        
        