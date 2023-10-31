class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        
        ans = [pref[0]]
        prefix_xor = pref[0]
        
        for i in range(1,len(pref)):
            
            temp_xor = pref[i] ^ prefix_xor
            ans.append(temp_xor)
            prefix_xor ^= temp_xor
         
        return ans
            
        
        