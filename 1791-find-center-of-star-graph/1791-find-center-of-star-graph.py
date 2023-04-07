class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
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
        for i in d:
            if len(d[i]) == len(edges):
                return i
            
            
        