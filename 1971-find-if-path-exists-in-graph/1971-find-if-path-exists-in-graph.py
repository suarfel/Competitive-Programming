class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        d = {}
        for i in edges:
            if i[0] in d:
                d[i[0]].append(i[1])
            else:
                d[i[0]] = [i[1]]
            if i[1] in d:
                d[i[1]].append(i[0])
            else:
                d[i[1]] = [i[0]]
        print(d)
        temp = False
        def dfs(vertex, visited):
            if vertex == destination:
                return True
            visited.add(vertex)
            for neighbour in d[vertex]:
                if neighbour not in visited:
                    r = dfs(neighbour, visited)
                    if r:
                        return True
            return False
        
        return  dfs(source,set())
        
        
        