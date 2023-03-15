class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        if n == 1 or  k == 1:
            return 0
        if k%2 == 1:
            temp = self.kthGrammar(n-1,(k+1)//2)
            return temp
        if k%2 == 0:
            temp = self.kthGrammar(n-1,k//2)
            return abs(temp-1)
            
            
        
        
        