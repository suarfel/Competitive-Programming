class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        
        count = len(nums)
        arr = []
        
        for idx,num  in enumerate(nums):
            if num == val :
                nums[idx] = float('inf')
                count -= 1
            else:
                arr.append(num)
                
        assert count == len(arr)
        
        arr.sort()
        nums.sort()
        
        for idx,num in enumerate(arr):
            assert nums[idx] == arr[idx]
        
        return count
            
            
        
        
                
        