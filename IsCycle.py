from typing import List
from collections import *
class Solution:
    #Function to detect cycle in an undirected graph.
	def isCycle(self, V: int, adj: List[List[int]]) -> bool:
	    
	    
	    visited = set()
	    isCycle = False
	    
	    for  i in range(V):
	        if i not in visited:
                queue = deque([(i,None)])
                visited.add(i)
                
                while queue :
                    
                    node,parent = queue.popleft()
                    
                    for neghibour in adj[node]:
                        
                        if neghibour not in visited:
                            queue.append((neghibour,node))
                            visited.add(neghibour)
                            
                        elif neghibour in visited:
                           if neghibour != parent:
                               isCycle  = True
                               break
	    return isCycle
	                  
