class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
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
        l = len(stack)
        for i in range(l):
            temp = stack.pop()
            right = len(heights)
            left = stack[-1] if stack else -1
            area = (right - left -1)*heights[temp]
            if area > max_area:
                max_area = area
        return max_area
            
        
                
                
        