class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        for i in range(len(nums1)):
            n=nums2.index(nums1[i])
            for j in range(n,len(nums2)):
                if nums1[i] < nums2[j]:
                    nums1[i]=nums2[j]
                    break
                elif nums1[i] >= nums2[j] and j ==(len(nums2)-1):
                    nums1[i]=-1
        return nums1
            