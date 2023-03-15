class DataStream:

    def __init__(self, value: int, k: int):
        self.value = value
        self.k = k
        self.nums = deque()
        self.count = 0
    def consec(self, num: int) -> bool:
        while self.nums and (len(self.nums) >= self.k or num != self.value):
            self.count -= 1
            self.nums.popleft()
        if num == self.value:
            self.nums.append(num)
        if num == self.value:
            self.count += 1
        if self.k == self.count:
            return True
        return False