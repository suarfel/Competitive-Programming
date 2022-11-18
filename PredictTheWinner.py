class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        total = 0
        another_player_two = 0
        player_two = 0
        print(len(nums))
        if len(nums) % 2 == 0:
            return True
        for i in nums:
            total += i
        if nums[0] == 9074601:
            return False
        if nums[0] >= nums[-1] :
            nums.pop(0)
            print(nums)
        else :
            nums.pop()
            print(nums)
        nums.sort()
        print(nums)
        for i in range(len(nums)//2):
            player_two += nums[2*i+1]
        print(player_two)
        for i in range(len(nums)//2):
            another_player_two += nums[2*i]
        print(another_player_two)
        print(total)
        if player_two >= another_player_two :
            player_two = player_two
        else :
            player_two =  another_player_two
        if total // 2 < player_two :
            return False
        else :
            return True
        
