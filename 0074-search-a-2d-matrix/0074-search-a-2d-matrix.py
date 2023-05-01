class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        valid = False
        
        for lis in matrix:
            
            if target in lis:
                
                valid = True
                
        return valid
        