def carFleet(target, position , speed):
        n = len(position)
        time = []
        nums = sorted(zip(position, speed), reverse=True)
        print(nums)
        for x, y in nums:
            time.append((target-x) / y)
        print(time)
        ans, prev = 0, 0
        for i in range(n):
            if time[i] > prev:
                ans += 1
                prev = time[i]
        
        return ans
print(carFleet(15,[3,5,6],[6,3,5]))