class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        
        graph = defaultdict(list)
        for i in range(len(isConnected)):
            for j in range(len(isConnected[0])):
                if isConnected[i][j] == 1:
                    graph[i+1].append(j+1)
                
        self.visited = set()
        def dfs(source):
            
            self.visited.add(source)
            for node in graph[source]:
                if node not in self.visited:
                    dfs(node)
                    
        count = 0          
        for node in graph:
            if node not in self.visited:
                dfs(node)
                count += 1
        return count
            
            
        