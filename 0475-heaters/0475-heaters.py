class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        max_radius= []
        heaters.sort()
        for i in houses:
            low = 0 
            high = len(heaters) -1
            print(i)
            while low +1 < high:
                mid = (low + high)//2
                if heaters[mid] <= i:
                    low = mid 
                else:
                    high = mid   
            minimum = min(abs(heaters[low] - i), abs(heaters[high] - i))
            max_radius.append(minimum)
            
        return max(max_radius)