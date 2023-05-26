class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        
        arr.sort()
        
        for index,val in enumerate(arr):
            if index == 0 :
                arr[index] = 1
            elif arr[index] > arr[index-1]+1:
                arr[index] = arr[index-1]+1
        return arr[-1]
                
        