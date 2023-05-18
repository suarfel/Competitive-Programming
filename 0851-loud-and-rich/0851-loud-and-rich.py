class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        
        graph = defaultdict(list)
        in_degree = {i : 0 for i in range(len(quiet))}
        quiet_graph = {quiet[i]: i  for i in range(len(quiet))}
        
        for edge in richer:
            graph[edge[0]].append(edge[1])
            in_degree[edge[1]] += 1
        
        queue = deque([])
        ans = [i for i in range(len(quiet))]
        
        for node in in_degree:
            if in_degree[node] == 0:
                queue.append(node)
                
        while queue:
            node = queue.popleft()
            
            for neghibour in graph[node]:
                
                if quiet[neghibour] > quiet[node]:
                    ans[neghibour] = quiet_graph[quiet[node]]
                    quiet[neghibour] = quiet[node]
                    
                in_degree[neghibour] -= 1
                if in_degree[neghibour] == 0:
                    queue.append(neghibour)
        return ans
                
                
                