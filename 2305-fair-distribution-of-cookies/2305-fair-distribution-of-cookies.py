class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        
        ans = float("inf")
        sum_arr = [0]*k
        ans_list = []
        
        def back_track(idx):
            
            if idx >= len(cookies):
                nonlocal ans
                ans = max(sum_arr)
                ans_list.append(ans)
                return
            
            for i in range(k):
                if i > 0 and idx == 0:
                    return
                sum_arr[i] += cookies[idx]
                back_track(idx + 1)
                sum_arr[i] -= cookies[idx]
        
        back_track(0)
        return min(ans_list)
                
                
        
        