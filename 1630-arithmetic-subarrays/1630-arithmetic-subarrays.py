class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        boolean_list = []
        for i in range(len(l)):
            temp = nums[l[i]:r[i]+1]
            temp.sort()
            if len(temp) == 1:
                boolean_list.append(True)
            else:
                constant = temp[1] - temp[0]
                for i in range(1,len(temp)):
                    if temp[i] - temp[i-1] != constant:
                        boolean_list.append(False)
                        break
                    elif temp[i] - temp[i-1] == constant and i == len(temp)-1:
                        boolean_list.append(True)
        return boolean_list

        