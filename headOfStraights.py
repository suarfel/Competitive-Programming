class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0 :
            return False
        if groupSize == 1 :
            return True
        valueDict = {}
        handSet = []
        for i in hand :
            if i not in valueDict:
                valueDict[i] = 1
                handSet.append(i)
            else :
                valueDict[i] += 1
        handSet.sort()
        temp = []
        while len(handSet) != 0:
            j  = 0
            for k in range(groupSize-1) :
                if len(handSet) >= groupSize and handSet[j] == handSet[j+1]-1:
                    valueDict[handSet[j]] -= 1
                    if valueDict[handSet[j]] == 0 :
                        temp.append(j)
                    j += 1 
                else :
                    return False
                if j == groupSize - 1 :
                    valueDict[handSet[j]] -= 1
                    if valueDict[handSet[j]] == 0 :
                        temp.append(j)
                    for i in range(len(temp)) : 
                        handSet.pop(temp[-(i+1)]) 
                    temp = [] 
        return True
