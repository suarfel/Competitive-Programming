class Solution:
    def maxArea(self, height: List[int]) -> int:
        i, j= 0, len(height) - 1 
        area =0
        for w in range(len(height) - 1, 0, -1):
            if height[i] < height[j]: 
                area = max(area, height[i] * w)
                i += 1
            else: 
                area  = max(area, height[j] * w)
                j -= 1
        return area
        # i = 0
        # j= len(height) - 1
        # area = 0
        # while i < len(height)-1:
        #     if  height[i] < height[j] and min(height[i],height[j])*(j-i) > area:
        #         area = min(height[i],height[j])* (j-i)
        #         i += 1
        #         j = len(height) - 1 
        #     elif height[i] >= height[j] and min(height[i],height[j])* (j-i) > area:
        #         area = min(height[i],height[j])* (j-i)
        #         j -= 1
        #     else:
        #         j -= 1
        #     if j == i:
        #         i += 1
        #         j = len(height) - 1 
                
                
                
            
            
            # j= i+1
            # while j < len(height):
            #     if min(height[i],height[j])* (j-i) > area:
            #         area =  min(height[i],height[j])* (j-i)  
            #     j += 1
            # i += 1
        # return area