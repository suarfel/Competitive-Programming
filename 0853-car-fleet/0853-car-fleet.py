class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        target_left = []
        collection=[]
        left = []
        for i in position:
            target_left.append(target-i)
        for i in range(len(position)):
            collection.append([target_left[i],speed[i]])
        collection.sort()
        for i,j in collection:
            left.append(i/j)
        size_fleet = 0 
        start = 0
        for i in left:
            if i > start:
                size_fleet += 1
                start = i  
        return size_fleet 