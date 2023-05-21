class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        
        rep =  {}
        inherit = {}
        rank = {}
        for i in range(len(accounts)):
            for j in range(1,len(accounts[i])):
                rep[accounts[i][j]] = accounts[i][j]
                inherit[accounts[i][j]] = accounts[i][0]
                rank[accounts[i][j]] = 0
        
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
        
        for i in range(len(accounts)):
            for j in range(1,len(accounts[i])-1):
                union(accounts[i][j],accounts[i][j+1])
                
        ans = defaultdict(set)
        for i in range(len(accounts)):
            for j in range(1,len(accounts[i])):
                temp = find(accounts[i][j])
                ans[temp].add(accounts[i][j]) 
        arr = defaultdict(list)
        a = []
        for item in ans:
            l = list(ans[item])
            l.sort()
            l = [inherit[item]] + l
            a.append(l)
        return a
            
        
        
        
        
        