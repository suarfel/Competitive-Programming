class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        ans = []
        arr = [0]

        def dfs(source,visited):

            visited.add(source)
            for i in graph[source]:
                if i == len(graph)-1:
                    arr.append(i)
                    ans.append(list(arr))
                    arr.pop()
                else:
                    arr.append(i)
                    dfs(i,visited)
                    arr.pop()
        dfs(0,set())
        return ans
        