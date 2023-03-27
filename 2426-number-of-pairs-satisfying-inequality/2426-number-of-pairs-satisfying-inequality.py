class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], diff: int) -> int:
        nums3 = []
        self.count = 0
        for i in range(len(nums1)):
            nums3.append(nums1[i]-nums2[i])
        def merge(left,right):
            result = []
            i = 0
            j = 0
            while i < len(left)  or j < len(right):
                if i < len(left)  and j < len(right):
                    if left[i] > right[j]:
                        result.append(right[j])
                        j += 1
                    else:
                        result.append(left[i])
                        i += 1
                elif i < len(left) and j >= len(right):
                    result.append(left[i])
                    i += 1
                else:
                    result.append(right[j])
                    j += 1
            return result


        def mergeSort(left, right, arr):
            if left == right:
                return [arr[left]]
            mid = left + (right - left) // 2
            left_half = mergeSort(left, mid, arr)
            right_half = mergeSort(mid + 1, right, arr)
            
            
            i = j = 0
            while i < len(left_half) and j < len(right_half):
                if left_half[i] <= right_half[j] + diff:
                    self.count += len(right_half) - j  
                    i += 1
                else:
                    j += 1
            return merge(left_half, right_half)
        mergeSort(0,len(nums3)-1,nums3)
        return self.count
        