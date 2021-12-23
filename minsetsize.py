class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        list1 =[]
        dict1={}
        temp = len(arr)
        count = 0
        arr.sort()
        for i  in arr:
            dict1[i]=0
        for i in arr:
            dict1[i] += 1
        for i in dict1:
            list1.append(dict1[i])
        list1.sort()
        list1.reverse()
        for i in range(temp):
            if count >= temp//2:
                return i
            else:
                count += list1[i]
            
        