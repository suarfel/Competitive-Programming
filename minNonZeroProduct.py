class Solution:
    def minNonZeroProduct(self, p: int) -> int:
        
        MOD = 10**9+7

        
        max_mod = (pow(2, p, MOD)-1)%MOD   

        return (max_mod*pow( (max_mod-1)%MOD ,(pow(2, p-1, MOD-1)-1) % (MOD-1), MOD)) % MOD
        
        
#         z = pow(10,9) +7
#         x =(pow(2,p,z)-1)%z
#         print(x)
        
#         print(x)
#         return (x*(pow(x-1,x//2)))% z
       
        