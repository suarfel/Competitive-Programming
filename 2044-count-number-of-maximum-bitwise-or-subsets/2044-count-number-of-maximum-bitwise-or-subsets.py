class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        ans = self.backTrack(nums,[],[],0)
        d = {}
        maxV = 1
        for i in ans:
            temp = 0
            for j in range(len(i)):
                temp |= i[j]
            if maxV < temp :
                maxV = temp
            if temp not in d:
                d[temp] = 1
            else:
                d[temp] += 1
            
        return d[maxV]
                
    def backTrack(self,nums,ans,temp,index):
        if len(temp) != 0:
            ans.append(list(temp))
        for i in range(index,len(nums)):
            temp.append(nums[i])
            self.backTrack(nums,ans,temp,i+1)
            temp.pop()
        return ans
    
