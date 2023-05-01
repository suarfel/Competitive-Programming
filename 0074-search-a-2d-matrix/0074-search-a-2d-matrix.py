class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        low = 0
        high = len(matrix)*len(matrix[0])-1
        
        while 0 <= low <= high < len(matrix)*len(matrix[0]) :
            
            mid = (low + high)//2
            
            col = mid % len(matrix[0])
            row = mid // len(matrix[0])  
             
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] > target:
                high = mid - 1 
            else:
                low = mid + 1
                 
        return False
        