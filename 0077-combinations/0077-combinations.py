class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []
        def back_track(idx,temp):
            if len(temp) == k :
                ans.append(list(temp))
                return
            if idx < n+1:
                temp.append(idx)
                back_track(idx+1,temp)
                temp.pop()
                back_track(idx+1,temp)
            return ans
        return back_track(1,[])
                
         
            