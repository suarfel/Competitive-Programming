class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        distances = [float('inf') for i in range(n+1)]
        distances[k] = 0
        distances[0] = 0
        
        visited = set()        
        graph = defaultdict(list)
        
        for u,v,time in times:
            
            graph[u].append((v,time))
        
        priority_queue = [(0,k)]
        heapq.heapify(priority_queue)
        
        while priority_queue:
            
            current_time,current_node = heapq.heappop(priority_queue)
            
            if current_node in visited:
                continue
            
            visited.add(current_node)
            
            for neghibour,time in graph[current_node]:
                
                tim = time + current_time
                if distances[neghibour] > tim:
                    distances[neghibour] = tim
                    heapq.heappush(priority_queue,(tim,neghibour))
                    
        if float('inf') in distances:
            return -1
        return max(distances[1:])
        
        
        