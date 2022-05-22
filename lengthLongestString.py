class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        temp = []
        value = [0]
        size = 0
        i=0
        j=0
        while i < len(s):
             
            if s[j] not in temp:
                temp.append(s[j])
                size += 1
                if value[0] < size:
                    value[0] = size
                j += 1
            elif s[j] in temp:
                size=1
                temp= []
                temp.append(s[i]) 
                i += 1
                j = i
            if j == len(s)  :
                return value[0]
            
              
        return value[0]
        