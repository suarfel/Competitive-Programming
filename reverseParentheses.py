class Solution:
    def reverseParentheses(self, s: str) -> str:
        list1=[]
        list2=[]
        temp=[]
        temp1=[]
        for i in s:
            temp.append(i)
        for i in range(len(temp)):
            if temp[i]=="(":
                list1.append(i)
                temp[i]= 0
            if temp[i]==")":
                list2.append(i)
                temp[i]=0
    
        for i in range(len(list1)):
            temp[list1[-(i+1)]+1:list2[i]]=reversed(temp[list1[-(i+1)]+1:list2[i]])
        for i in temp:
            if i!=0:
                temp1.append(i)
        string = ''.join(str(item) for item in temp1)
     
        return string