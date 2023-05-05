class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        
        stones = [-x for x in stones]
        heapq.heapify(stones)
        
        while stones and len(stones) > 1:
            
             
            first_stone = -heapq.heappop(stones)
            second_stone = -heapq.heappop(stones)
           
            if first_stone == second_stone:
                continue
            else:
                heapq.heappush(stones,-(first_stone-second_stone))      
             
        if stones:
            
            return -stones.pop()
        return 0