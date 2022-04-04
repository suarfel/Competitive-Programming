class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        list =[]
        temp = sorted(arr)
        if temp ==arr:
            return list
        i=1
        j=len(arr)
        while i <= len(arr) :
            if i==j:
                arr.reverse()
                list.append(j)
                return list
            t=arr.index(i)
            arr[0:t+1]=reversed(arr[0:t+1])
            arr[0:len(arr)-(i-1)]=reversed(arr[0:len(arr)-(i-1)])
            list.append(t+1)
            list.append(len(arr)-(i-1))
            i = i+1