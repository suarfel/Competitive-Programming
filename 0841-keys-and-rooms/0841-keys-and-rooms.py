class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        
        graph = defaultdict(list)
        for i in range(len(rooms)):
            for j in rooms[i]:
                graph[i].append(j)
        
        visited = set([0])
        queue = deque([0])
        
        while queue:
            
            room = queue.popleft()
            
            for i in graph[room]:
                
                if i not in visited:
                    visited.add(i)
                    queue.append(i)
        return len(visited) == len(rooms)
            
            
        