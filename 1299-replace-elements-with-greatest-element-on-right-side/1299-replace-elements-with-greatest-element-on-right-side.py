class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        
        temp_max = -1
        
        for i in range(len(arr)-1,-1,-1):
            if temp_max < arr[i]:
                temp = arr[i]
                arr[i] = temp_max
                temp_max = temp
            else:
                arr[i] = temp_max
        return arr
        