class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []
        def back_track(idx,temp):
            if len(temp) == k :
                ans.append(list(temp))
                return
            for i in range(idx,n+1):
                temp.append(i)
                back_track(i+1,temp)
                temp.pop()
            return ans
        return back_track(1,[])
                
         
            