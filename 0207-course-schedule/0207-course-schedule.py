class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        in_coming = [0]*numCourses
        graph = defaultdict(list)
        
        for course,pre in prerequisites:
            graph[course].append(pre)
            in_coming[course] += 1

        arr = []
        for i in range(len(in_coming)):
            if in_coming[i] == 0:
                arr.append(i)
        cycle = False

        def dfs(source):
            nonlocal cycle
            
            for course in graph[source]:
                if visited[course] == 'white':
                    visited[course] = 'grey'
                    dfs(course)
                elif visited[course] == 'grey':
                    print(course)
                    cycle = True
            
            visited[source] = 'black'
        
        for index_course in range(numCourses):
            visited = ['white']*numCourses

            dfs(index_course)
        if cycle :
            return False
        return True
        