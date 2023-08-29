class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        
        ans = []
        p_counter = defaultdict(int)
        s_counter = defaultdict(int)
        left = 0
        
        for letter in p:
            p_counter[letter] += 1
        
        for i in range(len(s)):
            
            s_counter[s[i]] += 1
            
            if  len(p) == len(s[left:i+1]):
                if s_counter == p_counter:
                    ans.append(left)
                s_counter[s[left]] -= 1
                if s_counter[s[left]] == 0:
                    s_counter.pop(s[left])
                left += 1
                
        return ans
            
                    
                        
            
                        
                
            
            
        
            
        
        
        
            
        
        