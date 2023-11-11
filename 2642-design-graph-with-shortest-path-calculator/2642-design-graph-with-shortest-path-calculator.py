class Graph:

    def __init__(self, n: int, edges: List[List[int]]):
        
        self.graph = defaultdict(list)
        
        for frm,to,cost in edges:
            self.graph[frm].append((to,cost))

    def addEdge(self, edge: List[int]) -> None:
        
        frm,to,cost = edge
        self.graph[frm].append((to,cost))
        

    def shortestPath(self, node1: int, node2: int) -> int:
        
        ans = -1
        
        queue = [(0,node1)]
        heapq.heapify(queue)
        visited = set()
        
        while queue:
            
            cost,node = heapq.heappop(queue)
            
            if node == node2 :
                ans = cost
                break
            
            if node in visited:
                continue
            visited.add(node)
            
            for neghibour,cur_cost in self.graph[node]:
                heapq.heappush(queue,(cost + cur_cost,neghibour))
                
        return ans
    
            
        


# Your Graph object will be instantiated and called as such:
# obj = Graph(n, edges)
# obj.addEdge(edge)
# param_2 = obj.shortestPath(node1,node2)