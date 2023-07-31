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
        