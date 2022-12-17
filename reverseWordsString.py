class Solution:
    def reverseWords(self, s: str) -> str:
        string = '' 
        listStr = s.split()
        print(listStr)
        for i in range(len(listStr)):
            print(string)
            if i == 0 :
                string = listStr[i]  + string 
            else:
                string = listStr[i] +  ' ' + string  

        return string