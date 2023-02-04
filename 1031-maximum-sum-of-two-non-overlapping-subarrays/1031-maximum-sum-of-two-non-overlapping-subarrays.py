class Solution:
    def maxSumTwoNoOverlap(self, nums: List[int], firstLen: int, secondLen: int) -> int:
        def maxSum(nums,firstLen):
            firstSum = {} 
            sum = 0
            count = 0
            for i in range(firstLen):
                sum += nums[i]
            firstSum[firstLen-1] = sum
            for i in range(firstLen,len(nums)):
                sum -= nums[count]
                sum += nums[firstLen]
                firstSum[firstLen] = sum
                count += 1
                firstLen += 1
            return firstSum
        first = maxSum(nums,firstLen)
        second = maxSum(nums,secondLen)
        maxSum = 0
        for i in first:
            for j in second:
                if j > i + secondLen - 1 :
                    print(i,j)
                    if first[i] + second[j] > maxSum :
                        print(first[i],second[j])
                        maxSum = first[i] + second[j]
                        print(maxSum)
        print(True)
        for i in second:
            for j in first:
                if j > i+firstLen-1 :
                    if first[j] + second[i] > maxSum :
                        print(i,j)
                        maxSum = first[j] + second[i]
                        print(maxSum)
        return maxSum


            
            
        