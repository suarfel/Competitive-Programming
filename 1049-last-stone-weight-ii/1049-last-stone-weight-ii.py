class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
         
        dp = set([0])
        for i in range(len(stones)):
            temp = set()
            for val in dp:
                temp.add(abs(val+stones[i]))
                temp.add(abs(val-stones[i]))
            dp = temp
        return min(dp)   