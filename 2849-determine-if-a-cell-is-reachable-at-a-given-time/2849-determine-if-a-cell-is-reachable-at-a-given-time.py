class Solution:
    def isReachableAtTime(self, sx: int, sy: int, fx: int, fy: int, t: int) -> bool:
        
        x_diff = abs(sx-fx)
        y_diff = abs(sy-fy)
        
        if x_diff == 0 and y_diff == 0 and t == 1:
            return False
        ans = 0
        
        if x_diff >= y_diff :
            ans += y_diff
            x_diff -= y_diff
            y_diff = 0
        else:
            ans += x_diff
            y_diff -= x_diff
            x_diff = 0
        
        ans += max(x_diff,y_diff)
        
        
        
        return ans <= t
            
        