class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        s = ""
        if len(strs) == 1:
            return strs[0]  
        for i in range(len(strs[0])):
            for j  in range(1,len(strs)):
                print(i,strs[j])
                if i < len(strs[j]):
                    if strs[0][i]  == strs[j][i]:
                        if j == len(strs)-1:
                            s = s + strs[0][i]
                        continue
                    else:
                        return s
                else:
                    return s
        return s
            
        