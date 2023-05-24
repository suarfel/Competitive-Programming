class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        
        city_a = 0
        city_b = 0
        total = 0
        
        arr = []
        for i in range(len(costs)):
            arr.append([abs(costs[i][0]-costs[i][1]),i])
            
        arr.sort(reverse = True)
        
        for temp in arr:
            if len(costs)//2 > city_a and costs[temp[1]][0] >= costs[temp[1]][1]:
                city_a += 1
                total += costs[temp[1]][1]
            elif len(costs)//2 > city_b and costs[temp[1]][0] < costs[temp[1]][1]:
                city_b += 1
                total += costs[temp[1]][0]
            else:
                if len(costs)//2 == city_b:
                    city_a += 1
                    total += costs[temp[1]][1]
                else:
                    city_b += 1
                    total += costs[temp[1]][0]
     
                    
        return total
                
        