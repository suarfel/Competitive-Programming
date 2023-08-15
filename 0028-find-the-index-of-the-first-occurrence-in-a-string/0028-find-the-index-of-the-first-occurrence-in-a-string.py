class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        
        i,j = 0,0
        temp = i
        if len(haystack) < len(needle):
            return -1
        while i < len(haystack):
            if needle[j] == haystack[temp]:
                j += 1
                temp += 1
            else:
                j = 0
                i += 1
                temp = i
                
            if j == len(needle) :
                return i 
            if temp >= len(haystack):
                return -1
        return -1