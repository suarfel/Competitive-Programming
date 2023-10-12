class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        
        graph = defaultdict(list)
        
        for idx,val in enumerate(equations):
            
            graph[val[0]].append((val[1],values[idx]))
            graph[val[1]].append((val[0],1/values[idx]))
            
        def evaluate(start,end):
            
            visited = set()
            
            queue = deque([(start,1)])
            
            if start not in graph or end not in graph:
                return -1
            
            while queue:
                
                node,val = queue.pop()
                
                if node == end:
                    return val
                
                visited.add(node)
                
                for neghibour in graph[node]:
                    if neghibour[0] not in visited:
                        queue.append((neghibour[0],val*neghibour[1]))
                        
                     
            return -1
        
        ans = []
        
        for query in queries:
            
            ans.append(evaluate(query[0],query[1]))
            
        return ans
    
            