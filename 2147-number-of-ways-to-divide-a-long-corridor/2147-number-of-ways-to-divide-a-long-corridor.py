class Solution:
    def numberOfWays(self, corridor: str) -> int:
        
        
        num_ways = 0
        num_s = 0
        arr = []
        
        for idx in range(len(corridor)):
            
            if corridor[idx] == 'S':
                num_s += 1

                
            if num_s == 1 :
                arr.append(idx)
                
            if num_s == 2 :
                num_s = 0
                arr.append(idx)
        
        
        if num_s != 0 or not arr:
            return 0
        num_ways = 1
        for i in range(1,len(arr)-2):
            num_ways *= (arr[i+1]-arr[i])
        
        return num_ways % (10**9 + 7)
            
            
        