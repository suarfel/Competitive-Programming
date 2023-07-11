class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        
        
        left,top,right,bottom = 0,0,len(matrix[0])-1,len(matrix)-1
        ans = []
        
        def in_bound(left,right,top,bottom):
            return left <= right  and top <= bottom
        
        while left <= right  and top <= bottom :
            
            if in_bound(left,right,top,bottom):
                for i in range(left,right+1):
                    ans.append(matrix[top][i])
                top += 1
                
            if in_bound(left,right,top,bottom):
                for i in range(top,bottom+1):
                    ans.append(matrix[i][right])
                right -= 1
                
            if in_bound(left,right,top,bottom):
                for i in range(right,left-1,-1):
                    ans.append(matrix[bottom][i])
                bottom -= 1
            
            if in_bound(left,right,top,bottom):
                for i in range(bottom,top-1,-1):
                    ans.append(matrix[i][left])
                left += 1
            
        return ans
            
                        

            
            