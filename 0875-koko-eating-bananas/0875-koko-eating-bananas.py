class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low  =   1
        high =  max(piles)
        ans  = 1
        while low <= high:
            mid = (low + high)//2
            sum = 0 
            for i in piles:
                if i % mid != 0:
                    sum += i//mid + 1
                else:
                    sum += i//mid
            if sum > h:
                low = mid + 1
            elif sum <= h:
                high = mid-1
                ans = mid
        return ans
                 