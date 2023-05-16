class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        
        graph = defaultdict(list)
        in_degree = {v : 0 for v in range(n)}
        ans = defaultdict(set)
        
        for edge in edges:
            graph[edge[0]].append(edge[1])
            in_degree[edge[1]] += 1
            
        queue = deque([v for v in graph if in_degree[v] == 0])
        
        while queue:
            
            node = queue.popleft()
            
            for neghibour in graph[node]:
                if node in ans:
                    ans[neghibour] |= ans[node]  
                ans[neghibour].add(node)
                in_degree[neghibour] -= 1
                if in_degree[neghibour] == 0:
                    queue.append(neghibour)
        
        arr = []
        for i in range(n):
            if i in ans:
                temp = list(ans[i])
                temp.sort()
                arr.append(temp)
            else:
                arr.append([])
                
        return arr
                    
        
        
        
                
        