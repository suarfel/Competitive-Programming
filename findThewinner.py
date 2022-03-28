class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        li=[]
        for i in range(n):
            li.append(i+1)
        i = 0
        while len(li)!=1:
            i += k-1
            i = i % len(li)
            li.pop(i)
            
            
        return li[0]