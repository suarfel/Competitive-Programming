class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
      
        for index,task in enumerate(tasks):
            task.append(index)
        
        heapq.heapify(tasks)
        
        ans = []
        total_time = 0
        ava_tasks = []
        
        while tasks or ava_tasks:
          
            if total_time == 0:
                task = heapq.heappop(tasks)
                total_time =   task[0] + task[1]
                ans.append(task[2])
            elif not ava_tasks and tasks[0][0] > total_time:
                total_time = tasks[0][0]
            else:
                
                while tasks and tasks[0][0] <= total_time  :
                    task = heapq.heappop(tasks)
                    heapq.heappush(ava_tasks,(task[1],task[2]))

                if ava_tasks:
                    task = heapq.heappop(ava_tasks)
                    total_time += task[0]
                    ans.append(task[1])
                
        return  ans