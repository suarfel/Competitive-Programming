class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        ans = 1
        left = 0
        s_counter = defaultdict(int)
        max_counter = [0,'']
        
        for i in range(len(s)):
            
            s_counter[s[i]] += 1
            if s_counter[s[i]] >= max_counter[0]:
                max_counter = [s_counter[s[i]],s[i]]
            
            if i-left+1 > max_counter[0] + k: 
                s_counter[s[left]] -= 1
                if s[left] == max_counter[1]:
                    max_counter[0] -= 1
                if s_counter[s[left]] == 0:
                    s_counter.pop(s[left])
                    
                left += 1
                
            ans = max(ans,(i-left+1))
        return ans
                    
                
                
            