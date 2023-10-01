class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        
        satisfaction.sort()
        max_ = 0

        if satisfaction[-1] < 0:
            return max_
        
        for j in range(len(satisfaction)):
            temp_max = 0 
            mult = 0
            for i in range(j,len(satisfaction)):
                temp_max +=( mult+1)*satisfaction[i]
                mult += 1
                
            max_ = max(max_,temp_max) 
        return  max_
            
                
                
            
            
        