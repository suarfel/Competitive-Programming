class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        
        piles = [-i for i in piles]
        heapq.heapify(piles)

        for i in range(k):
            large = -heapq.heappop(piles)
            minus = floor(large/2)
            large -= minus
            heapq.heappush(piles,-large)
            
        return -sum(piles)