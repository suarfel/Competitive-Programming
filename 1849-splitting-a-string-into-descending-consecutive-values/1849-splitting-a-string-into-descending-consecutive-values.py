class Solution:
    def splitString(self, s: str) -> bool:
        for i in range(1,len(s)):
            if self.backTrack(s[i:],int(s[:i])):
                return True
    def backTrack(self,s,prev):
        if int(s) == prev-1:
            return True
        for i in  range(1,len(s)+1):
            temp = int(s[:i])
            if temp == prev -1 :
                if self.backTrack(s[i:],temp):
                    return True
        return False
         
                