class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        li =[]
        for i in nums:
            li.append(int(i))
        li.sort()
        li.reverse()
        return str(li[k-1])
        