class Solution:
    def maximumRequests(self, n: int, requests: List[List[int]]) -> int:
        
        ans = []
        temp_ans = []
        dict_count = defaultdict(int)
        
        def back_track(idx,count):
            if ans:
                for i in dict_count:
                    if dict_count[i] == 0:
                        count += 1
                if count == len(dict_count):
                    temp_ans.append(len(ans))
                
            
            for transfer in range(idx,len(requests)):
                
                dict_count[requests[transfer][1]] += 1
                dict_count[requests[transfer][0]] -= 1
                ans.append(requests[transfer])
                
                back_track(transfer + 1,0)
                
                dict_count[requests[transfer][1]] -= 1
                dict_count[requests[transfer][0]] += 1
                ans.pop()
            
        back_track(0,0)
        max_req = 0
        if temp_ans:
            max_req = max(temp_ans)
        return max_req
            
                
                
                
                