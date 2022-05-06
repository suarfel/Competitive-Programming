class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        list=[]
        for i in range(n):
            list.append(i+1)
        i = 0
        def winner(list,k,i):
            if len(list) ==1:
                return list
            else:
                i += k-1
                i = i % len(list)
                list.pop(i)
                winner(list,k,i)
        winner(list,k,i)
        print(list[0])

so =Solution()
so.findTheWinner(5,2)