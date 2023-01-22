class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        mapper = {0:1}
        temp,counter = 0,0
        for i in range(len(nums)):
            if nums[i]%2 != 0:
                temp+=1
            if temp-k in mapper:
                counter += mapper[temp-k]
            if temp in mapper:
                mapper[temp] +=1
            else :
                mapper[temp] = 1
        return counter
            


        

                            


                


       

                




