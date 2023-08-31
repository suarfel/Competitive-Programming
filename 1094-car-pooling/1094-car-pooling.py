class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        
        n = 1000
        pas_counter = [0 for _ in range(n+1)]
        
        for trip in trips:
            numPas,fro,to = trip
            if numPas > capacity:
                return False
            pas_counter[fro] += numPas
            pas_counter[to] -= numPas
        
        ans = pas_counter[0]
        
        for i in range(1,n):
            if ans > capacity:
                return False
            ans += pas_counter[i]
            
        return True
        
        