# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        
        self.ans = deque([])
        
        
        t = True
        while t:
            t = False
            
            for j in range(len(nestedList)):
                if type(nestedList[j]) != int and not nestedList[j].isInteger() :
                    self.ans += nestedList[j].getList()
                    t = True
                    
                else:
                    if type(nestedList[j]) == int:
                        self.ans.append(nestedList[j])
                    else:
                        self.ans.append(nestedList[j].getInteger())
            if not t:
                break
            nestedList = self.ans
            self.ans = deque()
         
        
    
    def next(self) -> int:
        return self.ans.popleft()
    
    def hasNext(self) -> bool:
        return len(self.ans)  > 0
        
        
         

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())