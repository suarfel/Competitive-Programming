"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        
        graph = defaultdict()
        for employee in employees:
            graph[employee.id] = employee
        
        self.importance = 0
        def dfs(employee,visited):
            
            visited.add(employee.id)
            self.importance += employee.importance

            for employee in employee.subordinates:
                
                if employee not in visited:
                    dfs(graph[employee],visited)
        dfs(graph[id],set())
        return self.importance
                    
                
                
            
            
        
        