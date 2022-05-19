class Solution:
    
    def longestSubarray(self, nums: List[int], limit: int) -> int:

        import heapq
        i = 0
        j = 0
        longest = 0
        min_heap = []
        heapq.heapify(min_heap)
        
        max_heap = []
        heapq.heapify(max_heap)
        
        while i < len(nums) and j < len(nums):
            heapq.heappush(min_heap, (nums[j],j))
            heapq.heappush(max_heap, (-1*nums[j], j))
            
            while abs(min_heap[0][0] - -1*max_heap[0][0]) > limit:
                # You have either encountered a new min or max hence change 
                # accordingly without mono queue
                if j == max_heap[0][1]:
                    while abs(min_heap[0][0] - -1*max_heap[0][0]) > limit:

                        _, i = heapq.heappop(min_heap)
                        while min_heap[0][1] < i:
                            heapq.heappop(min_heap)
                        i += 1

                elif j == min_heap[0][1]:
                    while abs(min_heap[0][0] - -1*max_heap[0][0]) > limit:
                        _, i = heapq.heappop(max_heap)
                        while max_heap[0][1] < i:
                            heapq.heappop(max_heap)
                        i += 1

            longest = max(longest, (j-i)+1)
            j+=1
            return longest