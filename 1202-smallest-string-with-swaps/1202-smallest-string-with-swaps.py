class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        
        s = list(s)
        rep = {i : i for i in range(len(s))}
        parent = {i : s[i] for i in range(len(s))}
        rank = {i : 0 for i in range(len(s))} 
        
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
        
        for pair in pairs:
            union(pair[0],pair[1])
     
        ans = defaultdict(list)
        for i in range(len(s)):
            temp = find(i)
            ans[temp].append(parent[i])
            
        for key in ans:
            l = ans[key]
            l.sort(reverse=True)
            ans[key] = l
            
        for i in range(len(s)):
            temp = find(i)
            s[i] = ans[temp].pop()
            
        return ''.join(s)