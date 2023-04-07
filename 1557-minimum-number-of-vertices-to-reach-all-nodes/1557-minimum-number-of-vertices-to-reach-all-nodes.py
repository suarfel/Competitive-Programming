class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        d = set()
        ans = []
        for i in edges:
            d.add(i[1])
        for i in range(n):
            if i not in d:
                ans.append(i)
        return ans
            
            