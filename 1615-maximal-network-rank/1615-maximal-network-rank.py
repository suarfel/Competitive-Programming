class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        
        d = defaultdict(set)
        max_rank = 0
        for i in roads:
            d[i[0]].add(i[1])
            d[i[1]].add(i[0])
        for i in range(n):
            for j in range(i+1,n):
                if i in d[j]:
                    if len(d[i]) + len(d[j])-1 > max_rank:
                        max_rank = len(d[i]) + len(d[j])-1
                else:
                    if len(d[i]) + len(d[j]) > max_rank:
                        max_rank = len(d[i]) + len(d[j])
        return max_rank
                    
                
        
        
        