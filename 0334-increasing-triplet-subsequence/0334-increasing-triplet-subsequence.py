class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        
        num_one = float('inf')
        num_two = float('inf')
        
        for num in nums:
            if num <= num_one:
                num_one = num
            elif num <= num_two:
                num_two = num
            else:
                return True

        return False
        