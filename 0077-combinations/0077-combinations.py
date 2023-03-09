class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []
        temp = []
        return self.backTrack(n,k,temp,ans,1)
    def backTrack(self,n,k,temp,ans,index):
        if len(temp) == k:
            ans.append(list(temp))
        else:
            for i in range(index,n+1):
                temp.append(i)
                self.backTrack(n,k,temp,ans,i+1)
                temp.pop()
        return ans
         
            