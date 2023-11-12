class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        
        graph = defaultdict(set)
        
        for group,route in enumerate(routes):
            for i in range(len(route)):
                graph[route[i]].add(group)
                
        queue = deque([(source,0)])
        visited = set()
        ans = -1
        
        if source not in graph or target not in graph:
            return ans
        
        while queue:
            
            route,min_buses = queue.popleft()
            
            if route == target :
                ans = min_buses
                break
            
            if route in visited:
                continue
            visited.add(route)
            
            for group in graph[route]:
                for neghibour in routes[group]:
                    queue.append((neghibour,min_buses+1))
                routes[group] = []
                
        return ans
            
        
        