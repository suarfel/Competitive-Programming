class Solution:
    def knightDialer(self, n: int) -> int:
        
        arr = [1 for _ in range(10)]
        
        for i in range(1,n):
            
            cur = [0 for _ in range(10)]
            
            cur[0] = arr[4]  + arr[6]
            cur[1] = arr[6] + arr[8]
            cur[2] = arr[9] + arr[7]
            cur[3] = arr[4] + arr[8]
            cur[4] = arr[3] + arr[9] + arr[0]
            cur[5] = 0
            cur[6] = arr[1]  + arr[7] + arr[0]
            cur[7] = arr[2] + arr[6]
            cur[8] = arr[3] + arr[1]
            cur[9] = arr[4] + arr[2]
        
            arr = cur
            
    
        return sum(arr)%(10**9 + 7)
        