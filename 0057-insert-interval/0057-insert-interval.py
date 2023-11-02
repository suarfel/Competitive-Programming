class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        ans = []
        inserted = False
        
        for idx,interval in enumerate(intervals):
            
            left,right = interval
            if not inserted:
                new_left,new_right = newInterval
                if new_right < left:
                    inserted = True
                    ans.append(newInterval)
                    ans.append(intervals[idx])
                elif  new_left <= right :
                    intervals[idx] = [min(new_left,left),max(new_right,right)]
                    inserted = True
                    ans.append(intervals[idx])
                else:
                    ans.append(interval)
            else:
                if left <= ans[-1][1]:
                    ans[-1][1] = max(ans[-1][1],right)
                else:
                    ans.append(interval)
                    
        if ans and ans[-1][1] < newInterval[0]:
            ans.append(newInterval)
            
        if not ans:
            return [newInterval]
        return ans
                    
                
                
            
            
        