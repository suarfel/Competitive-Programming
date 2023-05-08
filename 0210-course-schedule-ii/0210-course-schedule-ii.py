class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        incoming_degree = [0] * numCourses
        
        graph = defaultdict(list)
        
        for course_one , course_two in prerequisites:
            graph[course_two].append(course_one)
            incoming_degree[course_one] += 1
            
            
        queue = deque([])
       
        for i in range(len(incoming_degree)):
        
            if 0 == incoming_degree[i] :
                queue.append(i)
         
        ans = []
        
        while queue :
            
            node = queue.popleft()
            ans.append(node)
            
            for neghibor in graph[node]:
                
                incoming_degree[neghibor] -= 1
                if incoming_degree[neghibor] == 0:
                    queue.append(neghibor)
        if len(ans) != numCourses:
            return []
            
        return ans
            
            
            
            
        