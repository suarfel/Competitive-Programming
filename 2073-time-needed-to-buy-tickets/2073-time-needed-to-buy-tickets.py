class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        
        counter = 0
        after = 0
        total = 0
        for i in range(len(tickets)):
            
            if tickets[k] <= tickets[i]:
                if k < i:
                    after += 1
                counter += 1 
            else:
                total +=  tickets[i]
        
        total += counter*tickets[k]
        return total - after
                
        