class Solution:
    def decodeString(self, s: str) -> str:
        str_word = []
        strin = '' 
        for i in s :
            if i.isdigit():
                if len(str_word) != 0 and str_word[-1].isdigit(): 
                    str_word[-1] = str_word[-1] + i
                elif len(str_word) != 0 and str_word[-1] == '[':
                    str_word[-1] = i    
                else:
                    str_word.append(i) 
            elif i == '[':
                str_word.append('[')
                continue
            elif i == ']' :
                print(str_word)
                if  str_word[-2].isdigit(): 
                    strin = str_word[-1]*int(str_word[-2])
                    str_word.pop(-1)
                    str_word.pop(-1)
                    str_word.append(strin)
                
                else:
                    strin = str_word[-2] + str_word[-1] 
                    str_word.pop(-1)
                    str_word.pop(-1)
                    str_word.append(strin)
            else :
                if len(str_word) !=0 and str_word[-1] == '[':
                    print(str_word)
                    str_word.pop()
                    print(str_word)
                if len(str_word) != 0 and  str_word[-1].isdigit() :
                    str_word.append(i)
                elif len(str_word) == 0:
                    str_word.append(i)
                else:
                    str_word[-1] += i
        for i in range(len(str_word)):
            if len(str_word) == 1:
                return str_word[0]
            elif  str_word[-2].isdigit() :
                strin = int(str_word[-2]) * str_word[-1] 
                str_word.pop(-1)
                str_word.pop(-1)
                str_word.append(strin)
            else :
                strin = str_word[-2] + str_word[-1] 
                str_word.pop(-1)
                str_word.pop(-1)
                str_word.append(strin)
                print(str_word)
            
       