 class Solution:
    def decodeString(self, s: str) -> str:
        str_list = []
        str_word = []
        for i in s:
            if i.isdigit():
                if len(str_list) > 0 and str_list[-1].isdigit():
                    str_list[-1] = str_list[-1] + i 
                else :
                    str_list.append(i)
                
            elif i == '[' or i==']':
                str_list.append(i)
            else:
                if len(str_list) > 0 and str_list[-1].isdigit() == False and str_list[-1] != '[' and str_list[-1] != ']' :
                    str_list[-1] = str_list[-1] + i
                else :
                    str_list.append(i)
            print()
       
        for i in str_list:
            if i.isdigit() :
                str_word.append(i)
            elif i == '[':
                continue
            elif i == ']':
                str_word[-1] = int(str_word[-2]) * str_word[-1]
                str_word.pop(-2)
                if len(str_word) > 1 :
                    if  not str_word[-2].isdigit() :
                        str_word[-2] = str_word[-2] + str_word[-1]
                        str_word.pop(-1)
            else :
                if len(str_word) == 0 :
                    str_word.append(i)
                elif str_word[-1] != '[' and str_word[-1] and not str_word[-1].isdigit():
                    str_word[-1] = str_word[-1] + i
                else:
                    str_word.append(i)
                   
        return str_word[0]
            
       
