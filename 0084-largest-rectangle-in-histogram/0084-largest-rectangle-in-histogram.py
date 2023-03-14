class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights.append(float('-inf'))
        stack = []
        max_area = 0
        for i,val in enumerate(heights):
            while stack and heights[stack[-1]] > val:
                temp = stack.pop()
                right = i
                left = stack[-1] if stack else -1
                area = (right - left -1)*heights[temp]
                if area > max_area:
                    max_area = area                 
            stack.append(i)
        return max_area
            
        
                
                
        