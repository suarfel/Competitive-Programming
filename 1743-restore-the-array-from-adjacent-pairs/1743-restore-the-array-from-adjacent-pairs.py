class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        
        
        adj_dict = defaultdict(list)
        ans = []
        
        
        for adjacent in adjacentPairs:
            first_pair,second_pair = adjacent
            adj_dict[first_pair].append(second_pair)
            adj_dict[second_pair].append(first_pair)
        
        queue = deque()
        
        for key in adj_dict:
            if len(adj_dict[key]) == 1 :
                queue.append(key)
                break
                
        visited = set()
        while queue :
            
            ele = queue.pop()
            if ele not in visited:
                visited.add(ele)
                ans.append(ele)
            else:
                continue
            
            for neghibour in adj_dict[ele]:
                queue.append(neghibour)
                
        return ans
                
            
            
            
            