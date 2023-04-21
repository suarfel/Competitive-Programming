class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row = set()
        col = set()
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == 0:
                    row.add(i)
                    col.add(j)
        row = list(row)
        row.sort()
        
        for i in row:
            for j in range(len(matrix[i])):
                matrix[i][j] = 0
        
        col = list(col)
        col.sort()
        for i in col:
            for j in range(len(matrix)):
                matrix[j][i] = 0
        
        
        
                
                
        
                    
        