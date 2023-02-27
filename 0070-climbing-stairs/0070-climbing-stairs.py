class Solution:
    def climbStairs(self, n: int) -> int:
        number_ways = [1,2]
        for i in range(2,n):
            number_ways.append(number_ways[i-1] + number_ways[i-2])
            print(number_ways)
        print(True)
        if n == 1 or n==2:
            return n
        return number_ways[-1]
        
        
        
            
        