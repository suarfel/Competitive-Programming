class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
            li = []
            temp = len(changed)
            if len(changed)%2 != 0:
                return li
            if [0]*temp == changed:
                return [0]*(temp//2)
            changed.sort()
            for i in range(len(changed)//2):
                if changed[0]*2 in changed[1:]:
                    li.append(changed[0])
                    changed.remove(changed[0]*2)
                    changed.pop(0)
                else:
                    return []
            if len(changed) == 0 :
                return li
            else :
                return []
             
        