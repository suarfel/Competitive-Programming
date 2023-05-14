class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        
        ans = []
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                ans.append(matrix[i][j])
        
        ans = heapq.nsmallest(k,ans)
        
        return ans[-1]
                
        
#         if k%len(matrix[0]) == 0:
#             row = k//len(matrix[0]) - 1 
#             col = len(matrix[0]) -1
#         else:            
#             row = k//len(matrix[0])  
#             col = k%len(matrix[0]) -1   
          
#         value = matrix[row][col]
#         max_one = -float('inf')
#         max_two = -float('inf')
        
#         if row > 0:
#             list_one = matrix[row-1]
#             list_one = [-i for i in list_one]
#             heapq.heapify(list_one)
#             max_one = -heapq.heappop(list_one)
            
#         if col > 0 :
#             list_two = matrix[col-1]
#             list_two = [-i for i in list_two]
#             heapq.heapify(list_two)
#             max_two = -heapq.heappop(list_two)
            
#         value =  max(max_one,value)
#         value =  min(max_two,)

        