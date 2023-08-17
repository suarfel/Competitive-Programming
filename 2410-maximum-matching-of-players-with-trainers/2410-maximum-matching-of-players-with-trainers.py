class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        
        max_match = 0
        players.sort()
        trainers.sort()
        
        i,j = 0,0
        
        while i < len(players) and j < len(trainers):
            if players[i] <= trainers[j]:
                max_match += 1
                i += 1
                j += 1
            else:
                j += 1
        return max_match
            
            
        
        