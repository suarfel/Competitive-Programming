class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        str_num = str(num)
        count  = 0
        for i in range(len(str_num)-k+1):
            print(str_num[i:k])
            if int(str_num[i : i + k]) != 0 and num % int(str_num[i : i + k]) == 0:
                count += 1
        return count            


            
            

