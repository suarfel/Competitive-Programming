class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        
        
        arr = []
        arr_choice = ['0' , '1']
        size = len(nums)
        
        def backtrack(s):
            
            if len(s) == size :
                arr.append(s)
                return 
            
            for ele in arr_choice:
                 
                backtrack(s + ele)
        
        backtrack("")
        
        for num in arr:
            if num not in nums:
                return num
            
        