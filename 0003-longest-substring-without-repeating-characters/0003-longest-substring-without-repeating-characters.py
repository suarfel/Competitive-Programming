class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i,j = 0 ,0
        counter = 0
        checkSet = set()
        while i < len(s) :
            if len(s) > j and s[j] not in checkSet:
                checkSet.add(s[j])
                j += 1
            else :
                if len(checkSet) > counter :
                    counter = len(checkSet)
                checkSet = set()
                i += 1
                j = i
        return counter






