class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        def reverse(s,i,j):
            if i >= j:
                return s
            else:
                s[i],s[j] = s[j],s[i]
                
                reverse(s,i+1,j-1)
        return reverse(s,0,len(s)-1)