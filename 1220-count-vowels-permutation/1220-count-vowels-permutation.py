class Solution:
    def countVowelPermutation(self, n: int) -> int:
        # vowel map holds the valid followers of the vowels
        vowel_map = defaultdict(set)
        vowel_map[0] = {1}
        vowel_map[1] = {0,2}
        vowel_map[2] = {0,1,3,4}
        vowel_map[3] = {2,4}
        vowel_map[4] = {0}
        
        m = 5 # number of vowels
        dp = [[0]*m for i in range(n)] # Two dimensional dp array 
        
        for i in range(m):
            dp[0][i] = 1
        
        for i in range(1,n):
            for j in range(m):
                for vowel in vowel_map[j]:
                    dp[i][j] += dp[i-1][vowel]
        
        
        return sum(dp[-1])%(pow(10,9)+7)
                
                
                
                
                
            
        
            
        
        
        
        