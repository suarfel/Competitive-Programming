class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        queue = deque()
        ans = []
        for i,val in enumerate(nums):
            while  queue and nums[queue[-1]] < val:
                queue.pop()
            queue.append(i)
            if i >= k - 1:
                left = i+1 - k
                while queue[0] < left:
                    queue.popleft()
                ans.append(nums[queue[0]])
        return ans
                
                