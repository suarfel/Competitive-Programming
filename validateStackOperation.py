class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        i = 0 
        temp = []
        for j in pushed:
            temp.append(j)
            while temp and i < len(popped) and temp[-1] == popped[i]:
                temp.pop()
                i += 1
                
        if i == len(popped):
            return True
        else:
            return False
                    