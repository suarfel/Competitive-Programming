class Solution:
    def maxLength(self, arr: List[str]) -> int:
        temp = []
        ans =  []
        ans = self.backTrack(arr,ans,temp,0)
        count = 0
        for i in ans:
            s = "".join(i)
            if len(s) == len(set(s)):
                if len(s) > count:
                    count = len(s)
        return  count
    def backTrack(self,arr,ans,temp,idx):
        ans.append(list(temp))
        for i in range(idx,len(arr)):
            temp.append(arr[i])  
            self.backTrack(arr,ans,temp,i+1)
            temp.pop()
        return ans
    # def backTrack(self,arr,temp,ans,idx):
    #     if len(temp) > len(ans):
    #         ans = str(temp)
    #     for i in range(idx,len(arr)):
    #         if len(temp) == 0 or len(temp + arr[i]) == len(set(temp + arr[i])):
    #             temp += arr[i]
    #             self.backTrack(arr,temp,ans,i+1)
    #     # print(ans) 
    #     return ans
        