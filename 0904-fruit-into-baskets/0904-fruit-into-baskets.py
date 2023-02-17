class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        count = 0 
        i= 0
        j=0
        dict_num = {}
        while j < len(fruits):
            if len(dict_num) ==2 and fruits[j] in dict_num:
                dict_num[fruits[j]] += 1
                j += 1
            elif len(dict_num) < 2:
                if fruits[j] in dict_num:
                    dict_num[fruits[j]] +=1
                else :
                    dict_num[fruits[j]] = 1
                j += 1
            else:
                while len(dict_num) == 2:
                    dict_num[fruits[i]] -= 1
                    if dict_num[fruits[i]] == 0:
                        del dict_num[fruits[i]]
                    i += 1

            temp = 0
            for k in dict_num:
                temp += dict_num[k]
            if temp > count :
                count = temp
            
        return count