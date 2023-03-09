class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []
        arr = []
        ans = self.backTrack(ans,n,arr,k,1)
        return ans
    def backTrack(self,ans,n,arr,k,add):
        if len(arr) == k:
            ans.append(arr.copy())
        else:
            for i in range(add,n+1):
                arr.append(i)
                self.backTrack(ans,n,arr,k,i+1)
                arr.pop()
        return ans
            