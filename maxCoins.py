class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        temp = len(piles)//3
        max = 0
        piles.sort()
        j = -2
        for i in range(temp):
            max += piles[j]
            j += -2
        return max
        