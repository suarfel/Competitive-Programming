class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        return self.recurse(n,k)[k-1]
    def recurse(self,n,k):
        if n == 1:
            return "0"
        else:
            temp = self.recurse(n-1,k) 
            i = self.invert(temp)
            i = i[::-1]
            s = temp + "1" + i
        return s
    def invert(self,s):
        st = []
        for i in range(len(s)):
            if s[i] == '0':
                st.append('1')
            else:
                st.append('0')
        return ''.join(st)