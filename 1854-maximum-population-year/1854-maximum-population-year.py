class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        
        arr = []
        
        for birth in range(1950,2051):
            arr.append((0,birth))
        
        for log in logs:
            first_idx = log[0] - 1950
            last_idx = log[1] - 1950
            arr[first_idx] = (arr[first_idx][0] + 1,arr[first_idx][1])
            arr[last_idx] = (arr[last_idx][0] - 1,arr[last_idx][1])
            
        
        for i in range(1,len(arr)):
            arr[i] = (arr[i][0] + arr[i-1][0],arr[i][1])
        
        population, early_year = 0,0
        
        for count,year in arr:
            
            if count > population:
                population = count
                early_year = year
            elif count == population and year < early_year:
                early_year = year
        
        return early_year
                
                
                
        
         
        

            
            