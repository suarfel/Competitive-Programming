class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        first_arr = []
        second_arr = []
        i  = 0
        while  i < len(arr)-1:
            if arr[i] < arr[i+1]:
                first_arr.append(arr[i])
            elif arr[i] == arr[i+1]:
                return False
            else:
                break
            i += 1
        if not first_arr:
            return False
        while  i < len(arr)-1:
            if arr[i] > arr[i+1]:
                second_arr.append(arr[i])
            else:
                return False
            i += 1
        if not second_arr:
            return False
        
            
        return True
            
            
            
            
        