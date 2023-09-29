class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        
        n,m = len(dungeon),len(dungeon[0])
 
        
        for i in range(n-1,-1,-1):
            for j in range(m-1,-1,-1):
                
                if i == n-1 and j == m-1 :
                    dungeon[i][j] = min(dungeon[i][j],0)*-1 + 1
                
                elif i == n-1:
                    dungeon[i][j] = max(dungeon[i][j+1]-dungeon[i][j],1)
                    
                elif j == m-1:
                    dungeon[i][j] = max(dungeon[i+1][j]-dungeon[i][j],1)
                
                else:
                    dungeon[i][j] = max(min(dungeon[i+1][j],dungeon[i][j+1])-dungeon[i][j],1)
        
        
        return dungeon[0][0]
                    
                    
                    
                        
                            
                            
                      