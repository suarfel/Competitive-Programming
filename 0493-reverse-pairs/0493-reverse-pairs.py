class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        
        self.count = 0
        
        def merge(left,right):
            
            result = []
            i = j = 0
            
            while i < len(left) or j < len(right):
                if i < len(left) and j < len(right):
                    if left[i] >= right[j]:
                        result.append(right[j])
                        j += 1
                    else:
                        result.append(left[i])
                        i += 1
                elif i < len(left):
                    result.append(left[i])
                    i += 1
                else:
                    result.append(right[j])
                    j += 1
            return result
        
        
        def mergeSort(left,right,arr):
            
            if left == right :
                return [arr[left]]
            mid = left + (right-left)//2
            left_half = mergeSort(left,mid,arr)
            right_half = mergeSort(mid+1,right,arr)
            
            i = len(left_half)-1
            j = len(right_half) - 1
            while i >=  0 and j >= 0 :
                if left_half[i] > 2*right_half[j]:
                    self.count += len(right_half) - (len(right_half)-j-1)
                    i -= 1
                else:
                    j -= 1  
            return merge(left_half,right_half)
        
        print(mergeSort(0,len(nums)-1,nums))
        return self.count
                
                    
                
            
            
            
           
        
        