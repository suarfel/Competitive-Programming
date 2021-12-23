class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        list1=[]
        list2=[]
        dict1={}
        nums.sort()
        for i  in nums:
            dict1[i]=0
        for i in nums:
            dict1[i] += 1
        for i in dict1:
            list1.append(dict1[i])
        list1.sort()
        list1.reverse()
        list1 =list1[0:k]
        for i in dict1:
            if dict1[i] in list1:
                list2.append(i)
        return list2
        
            
            
        