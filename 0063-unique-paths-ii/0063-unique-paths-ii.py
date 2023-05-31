class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        
        matrix = [[0 for i in range(len(obstacleGrid[0]))] for j in range(len(obstacleGrid))]
        matrix[0][0] = 1
        
        for i in range(len(obstacleGrid)):
            for j in range(len(obstacleGrid[0])):
                
                if obstacleGrid[i][j] == 1:
                    matrix[i][j] = 0
                elif i == 0 and j == 0:
                    continue
                elif i == 0 :
                    matrix[i][j] = matrix[i][j-1]
                elif j == 0 :
                    matrix[i][j] = matrix[i-1][j]
                else:
                    matrix[i][j] =   matrix[i-1][j] + matrix[i][j-1] 
                    
        return matrix[len(obstacleGrid)-1][len(obstacleGrid[0])-1]