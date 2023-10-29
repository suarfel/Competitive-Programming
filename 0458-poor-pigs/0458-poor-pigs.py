class Solution:
    def poorPigs(self, buckets: int, minutesToDie: int, minutesToTest: int) -> int:
        
        together = minutesToTest // minutesToDie + 1
        num_pigs = 0
        while buckets > pow(together,num_pigs):
            num_pigs += 1
        
        return num_pigs
        