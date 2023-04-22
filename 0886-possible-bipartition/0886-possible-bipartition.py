class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        
        graph = defaultdict(list)
        
        for i in dislikes:
            graph[i[0]].append(i[1])
            graph[i[1]].append(i[0])
                
        def dfs(source,visited,first_set,second_set):
            
            visited.add(source)
            v.add(source)
            
            for src in graph[source]:
                if src not in visited:
                    if source in first_set:
                        second_set.add(src)
                    else:
                        first_set.add(src)
                    temp = dfs(src,visited,first_set,second_set)
                    if not temp:
                        return temp
                else:
                    if src in first_set and source in first_set:
                        return False
                    elif src in second_set and source in second_set:
                        return False
            return True
        
        if len(dislikes) < 2:
            return True
        v = set()
        temp = True
        for node in graph:
            if node not in v:
                print(True)
                temp = dfs(node,set(),{node},set())
                if not temp:
                    return temp
        return temp
            
                        
                
        
        