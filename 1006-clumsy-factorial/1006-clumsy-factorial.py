class Solution:
    def clumsy(self, n: int) -> int:
        sumList = []
        addList = []
        numberList = []
        count = 0
        for i  in range(n,0,-1):
            count += 1
            if  count%4 == 0 and i != n:
                addList.append(i)
            else :
                numberList.append(i)
        count = 0
        value = 0
        for i in range(len(numberList)):
            if value % 3 == 0 :
                count = numberList[i]
                if i+1 == len(numberList):
                    sumList.append(count)
                value +=1
            elif value % 3 == 1 :
                count *= numberList[i]
                if i+1 == len(numberList):
                    sumList.append(count)
                value += 1
            elif value % 3 == 2:
                count //= numberList[i]
                sumList.append(count)
                value = 0
        totalSum = 0
        for i in range(len(sumList)):
            if i == 0:
                totalSum = sumList[i]
            else:
                totalSum -= sumList[i]
        for i in addList:
            totalSum += i
        return totalSum

        












