class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        dp = [[0]*len(text2) for _ in range(len(text1))]
        
        for i in range(len(text1)-1,-1,-1):
            
            for j in range(len(text2)-1,-1,-1):
                
                if i == len(text1)-1 and j == len(text2)-1:
                    if text1[i] == text2[j]:
                        dp[i][j] = 1
    
                elif i == len(text1)-1 :
                    if text1[i] == text2[j]:
                        dp[i][j] = max(1,dp[i][j+1])
                    else:
                        dp[i][j] = dp[i][j+1]
                        
                elif j == len(text2)-1:
                    if text1[i] == text2[j]:
                        dp[i][j] = max(1,dp[i+1][j])
                    else:
                        dp[i][j] = dp[i+1][j]
                else:
                    if text1[i] == text2[j]:
                        dp[i][j] = max(1 + dp[i+1][j+1],dp[i][j+1],dp[i+1][j])
                    else:
                        dp[i][j] = max(dp[i][j+1],dp[i+1][j])
        return dp[0][0]
                        
                    
                
        