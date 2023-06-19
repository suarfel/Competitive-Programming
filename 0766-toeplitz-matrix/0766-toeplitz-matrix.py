class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        
        i = j = 1
        
        while i < len(matrix):
            while j < len(matrix[0]):
                if matrix[i][j] != matrix[i-1][j-1]:
                    return False
                j += 1
            i += 1
            j = 1
        return True
                    
                
        