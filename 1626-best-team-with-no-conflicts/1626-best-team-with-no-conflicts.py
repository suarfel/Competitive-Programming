class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        
        arr = []
        ans = []
        for i in range(len(scores)):
            arr.append([ages[i],scores[i]])
            
        arr.sort()
        
        n= len(scores)
        
        for i in range(n):
            
            if i == 0:
                ans.append((arr[0][1],arr[0][0],arr[0][1]))
            
            else:
                max_ = arr[i][1]
                for j in range(len(ans)):
                    if (ans[j][1] < arr[i][0] and arr[i][1] > ans[j][0]) or (ans[j][1] == arr[i][0]) or (ans[j][0] == arr[i][1]):
                        max_ = max(max_,ans[j][2] + arr[i][1])
                ans.append((arr[i][1],arr[i][0],max_))
                
        max_ = ans[0][2]
        for ele in ans:
            max_ = max(max_,ele[2])
        
        return max_
            
                        
                
                
            
            
                
                
            
        
        
        
        