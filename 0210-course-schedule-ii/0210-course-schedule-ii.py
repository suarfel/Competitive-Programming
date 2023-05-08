class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        incoming_degree = [0] * numCourses
        graph = defaultdict(list)
        
        for course_one , course_two in prerequisites:
            graph[course_two].append(course_one)
            incoming_degree[course_one] += 1
              
        temp = []
       
        for i in range(len(incoming_degree)):
            if 0 == incoming_degree[i] :
                temp.append(i)
        
        cycle = False
        ans = []
        def dfs(current):
            nonlocal cycle
            for neghibor in graph[current]:
                
                if visited[neghibor] == 'white':
                    visited[neghibor] = 'grey'
                    dfs(neghibor)
                elif visited[neghibor] == "grey":
                    cycle = True
           
            if visited[current] != 'black':
                ans.append(current)
            visited[current] = 'black'
          
            
        visited = ['white'] * numCourses
        
        
        for course in temp:
            dfs(course)
            
         
        if len(ans) != numCourses or cycle:
            return []
        ans.reverse()
        return ans
        
        
        
            
        
        
        
            
         
      
      
            
            
            
            
        