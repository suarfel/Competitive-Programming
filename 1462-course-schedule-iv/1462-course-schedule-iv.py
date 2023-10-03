class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        
    
        is_prerequisites = [[float('inf')]*numCourses for _ in range(numCourses)]
        checker = {i for i in range(numCourses)}
        
        for requisite,course in prerequisites :
            is_prerequisites[requisite][course] = 0
            
        
        for i in range(numCourses):
            
            for j in range(numCourses):
                
                for k in range(numCourses):
                    
                    if is_prerequisites[j][i] + is_prerequisites[i][k] == 0:
                        
                        is_prerequisites[j][k] = is_prerequisites[j][i] + is_prerequisites[i][k]
        
        ans = []
        
        for query in queries:
            
            if is_prerequisites[query[0]][query[1]] == 0:
                ans.append(True)
            else:
                ans.append(False)
        
        return ans
        
        
        
        
                
            
            
        