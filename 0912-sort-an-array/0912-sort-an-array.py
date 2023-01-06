class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) > 1 :
            half = len(nums)//2

            firstHalf = nums[:half]
            secondHalf = nums[half:]

            self.sortArray(firstHalf)
            self.sortArray(secondHalf)
            i,j,k = 0,0,0
            while i < len(firstHalf) and j < len(secondHalf):
                if firstHalf[i] < secondHalf[j]:
                    nums[k] = firstHalf[i]
                    i += 1
                else : 
                    nums[k] = secondHalf[j]
                    j += 1
                k += 1
            
            while i < len(firstHalf):
                nums[k] = firstHalf[i]
                i += 1
                k += 1
            while j < len(secondHalf):
                nums[k] = secondHalf[j]
                j += 1
                k += 1
        return nums
        # listDict = {}
        # listSet = set()
        # sortedList = []
        # for i in nums:
        #     if i not in listDict:
        #         listDict[i] = 1
        #         listSet.add(i)
        #     else :
        #         listDict[i] += 1
        # for i in range(len(nums)):
        #     if len(listSet) == 0 :
        #         return sortedList
        #     minValue = min(listSet)
        #     listSet.remove(minValue)
        #     for j in range(listDict[minValue]):
        #         sortedList.append(minValue)
        # return sortedList
