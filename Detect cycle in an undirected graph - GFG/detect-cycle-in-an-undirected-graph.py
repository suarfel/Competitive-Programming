from typing import List
from collections import *
class Solution:
    #Function to detect cycle in an undirected graph.
	def isCycle(self, V: int, adj: List[List[int]]) -> bool:
	    
	    
	     
	     
	     def dfs(source):
	         
	         visited.add(source[0])
	         
	         for neghibour in adj[source[0]]:
	             if neghibour not in visited:
	                 return dfs((neghibour,source[0]))
	             elif neghibour in visited:
	                 
	                 if neghibour != source[1]:
	                     return True
	         return False
	         
	     
	     temp = False
	     
	     for i in range(V):
	         visited = set()
	         if i not in visited:
	             temp = dfs((i,None))
	             if temp:
	                 return temp

	     return temp
	                    
	            
	            
	        
	   
	        
	                    
	    
		#Code here


#{ 
 # Driver Code Starts
if __name__ == '__main__':

	T=int(input())
	for i in range(T):
		V, E = map(int, input().split())
		adj = [[] for i in range(V)]
		for _ in range(E):
			u, v = map(int, input().split())
			adj[u].append(v)
			adj[v].append(u)
		obj = Solution()
		ans = obj.isCycle(V, adj)
		if(ans):
			print("1")
		else:
			print("0")

# } Driver Code Ends