class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        l=len(tasks)
        tasks.sort()
        temp = {}
        list1=[]
        for i in tasks:
            if i not in temp:
                temp[i]=1
            else:
                temp[i] += 1
        for i in temp:
            list1.append(temp[i])
        list1.sort()
        Max = list1.pop()
        total_idle = (Max-1)*n
        while total_idle>0 and list1:
            total_idle = total_idle- min(Max -1,list1.pop())
        if total_idle<0:
            total_idle =0
        else :
            total_idle =total_idle
        return len(tasks) + total_idle
                
            
            
        
        