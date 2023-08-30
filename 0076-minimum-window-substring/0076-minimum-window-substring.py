class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        s_counter = defaultdict(int)
        t_counter = defaultdict(int)
        left = 0
        end = 0
        ans = ""
        
        for letter in t:
            t_counter[letter] += 1
            
        def checker(s_counter):
            temp = True
            for key in t_counter:
                if key in s_counter and t_counter[key] <= s_counter[key]:
                    continue
                else:
                    temp = False
            return temp
            
        
        while end < len(s):
            
            s_counter[s[end]] += 1
            
            while end-left+1 >= len(t) and checker(s_counter):
                s_counter[s[left]] -= 1
                if s_counter[s[left]] == 0:
                    s_counter.pop(s[left])
                                
                if ans == "" or end-left+1 < len(ans):
                    ans = s[left: end+1]

                left += 1
                
            end += 1
            
        return ans
    
                        
                        
                    
                    
                    
                    
                        
                        
        
        