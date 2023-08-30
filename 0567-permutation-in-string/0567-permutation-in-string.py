class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        s1_counter = defaultdict(int)
        s2_counter = defaultdict(int)
        left = 0
        
        if len(s1) > len(s2):
            return False
        
        for letter in s1:
            s1_counter[letter] += 1

        for i in range(len(s2)):
            s2_counter[s2[i]] += 1
            
            if i-left+1 == len(s1):
                if s1_counter == s2_counter:
                    return True
                s2_counter[s2[left]] -= 1
                if s2_counter[s2[left]] == 0:
                    s2_counter.pop(s2[left])
                left += 1
                
        return False
                
            
            