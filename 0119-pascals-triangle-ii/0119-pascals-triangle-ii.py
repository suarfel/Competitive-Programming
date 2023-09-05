class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        else:
            li = self.getRow(rowIndex-1)
            arr = [1]
            for i in range(1,len(li)):
                arr.append(li[i]+li[i-1])

            arr.append(1)
            return arr
 
