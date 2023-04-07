class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        d = defaultdict(list)
        for i in edges:
            d[i[0]].append(i[1])
            d[i[1]].append(i[0])
        for i in d:
            if len(d[i]) == len(edges):
                return i
            
            
        