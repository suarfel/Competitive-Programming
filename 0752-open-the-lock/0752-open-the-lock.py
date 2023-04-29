class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        
        
        deadends = set(deadends)
        
        
        def neghibors(node):
            print(node)
            x = list(node[0])
            arr = []
            
            for i in range(4):
                temp = node[i]
                if node[i] == '0':
                    node[i] = '9'
                    st = ''.join(node)
                    arr.append(st)
                    node[i] = '1'
                    st = ''.join(node)
                    arr.append(st)
                    node[i] = temp
                elif node[i] == '9':
                    node[i] = '0'
                    st = ''.join(node)
                    arr.append(st)
                    node[i] = '8'
                    st = ''.join(node)
                    arr.append(st)
                    node[i] = temp
                else:
                    node[i] = str(int(temp) + 1)
                    st = ''.join(node)
                    arr.append(st)
                    node[i] = str(int(temp) - 1)
                    st = ''.join(node)
                    arr.append(st)
                    node[i] = temp
            return arr
        
        if "0000" in deadends:
            return -1
        queue = deque([("0000",0)])
        visited = set(["0000"])
        ans = float('inf')
        
        while queue:
            node = queue.popleft()
            arr = neghibors(list(node[0]))
            
            if node[0] == target:
                if ans > node[1] :
                    ans = node[1]
            
            for nex in arr:
                
                if nex not in visited and nex not in deadends:
                    queue.append((nex,node[1]+1))
                    visited.add(nex)
                    
        if ans  == float('inf'):
            return -1
        return ans
                    
                
        
        
        
        