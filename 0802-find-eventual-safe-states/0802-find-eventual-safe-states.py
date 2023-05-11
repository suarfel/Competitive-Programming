class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        
        
        
        gra = defaultdict(list)
        in_coming = [0]* len(graph)
        
        for edge in range(len(graph)):
            for j in range(len(graph[edge])):
                gra[graph[edge][j]].append(edge)
                
        
        queue = deque([])
        
        
        for i in range(len(graph)):
            in_coming[i] = len(graph[i])
            if in_coming[i] == 0:
                queue.append(i)
               
        ans = []
        
        while queue:
            
            node  = queue.popleft()
            ans.append(node)
            
            for edge in gra[node]:
                
                in_coming[edge] -= 1
                if in_coming[edge] == 0:
                    queue.append(edge)
        ans.sort()
        return ans
            
            
            
 
        
        
        
        
        