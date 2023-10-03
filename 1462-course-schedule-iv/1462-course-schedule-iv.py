class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        
        graph = defaultdict(list)
        indegree = defaultdict(int)
        pre = defaultdict(set)
        
        for before,after in prerequisites:
            graph[before].append(after)
            indegree[after] += 1
        
        take_courses = []
        
        for course in range(numCourses):
            if indegree[course] == 0:
                take_courses.append(course)
        
        queue = deque(take_courses)
        
        while queue:
            
            node = queue.popleft()
            
            for ele in graph[node]:
                pre[ele].add(node)
                pre[ele] = pre[ele] | pre[node]
                
                indegree[ele] -= 1
                if indegree[ele] == 0:
                    queue.append(ele)
        
        ans = []
        for query in queries:
            if query[0] in pre[query[1]]:
                ans.append(True)
            else:
                ans.append(False)
                
        return ans
                
            
            
        