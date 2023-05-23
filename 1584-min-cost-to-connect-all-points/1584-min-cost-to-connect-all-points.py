class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        rep = {i : i for i in range(len(points))}
        rank = {i : 0 for i in range(len(points))}
        
        def find(x):
            root = x
            while root != rep[root]:
                root = rep[root]
            while x != root:
                parent  = rep[x]
                rep[x] = root
                x  = parent
            return root

    
        def union(x,y):
            rootX = find(x)
            rootY = find(y)
            
            if rootX == rootY:
                return 
            if rank[rootX] > rank[rootY]:
                rep[rootY] = rootX
            if rank[rootX] < rank[rootY]:
                rep[rootX] = rootY
            if rank[rootX] == rank[rootY]:
                rep[rootY] = rootX
                rank[rootX] += 1
        arr = []     
        for i in range(len(points)-1):
            for j in range(i+1,len(points)):
                manhatten = abs(points[i][0]-points[j][0]) + abs(points[i][1]-points[j][1])
                arr.append((manhatten,i,j))
                
        heapq.heapify(arr)
        
        result = 0
        while arr:
            ele = heapq.heappop(arr)
            if find(ele[1]) == find(ele[2]):
                continue
            else:
                union(ele[1],ele[2])
                result += ele[0]
        return result
                
                
                
            
            
    
                        
                
                    
                    
        