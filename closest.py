class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        closers= []*k 
        sizes= []*len(points)
        for i in points:
            sizes.append(i[0]**2 + i[1]**2)   
        sizes.sort()
        last_closer = sizes[k-1]
        for i in points:
            if i[0]**2 + i[1]**2 <= last_closer:
                closers.append(i)
        return closers