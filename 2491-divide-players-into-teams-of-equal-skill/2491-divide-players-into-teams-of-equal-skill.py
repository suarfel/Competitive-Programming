class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        team_sum = 0
        total = 0
        skill.sort()
        
        if len(skill) == 2 :
            return skill[0] * skill[1]
        i ,j = 0 , len(skill)-1
        team_sum = skill[0] + skill[-1]
        
        while i < j:
            if skill[i] + skill[j] != team_sum:
                return -1
            total += (skill[i] * skill[j])
            i += 1
            j -= 1
        
        return  total
            
            
        
         
        