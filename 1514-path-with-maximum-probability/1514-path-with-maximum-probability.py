class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        
        
        
        graph = defaultdict(list)
        
        for idx,edge in enumerate(edges):
            graph[edge[0]].append((edge[1],succProb[idx]))
            graph[edge[1]].append((edge[0],succProb[idx]))
      
        queue = [(float('inf'),start_node,0)]
        visited = set()
        heapq.heapify(queue)
        
        while queue:
            
            cur_prob,cur_node,total = heapq.heappop(queue)
            
            if cur_node == end_node:
                if cur_prob == float('inf'):
                    return 1
                else:
                    return -cur_prob

            if cur_node in visited:
                continue
            
            visited.add(cur_node)
            
            for neghibour in graph[cur_node]:
                if cur_prob == float('inf'):
                    heapq.heappush(queue,(-neghibour[1],neghibour[0],total + neghibour[1]))
                else:
                    val  = (total*neghibour[1])
                    heapq.heappush(queue,(-val,neghibour[0],val))
                    
        return 0
                    
                    
                
            
            

            
        