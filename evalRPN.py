class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack1=[]
        list1=["+", "-", "*", "/"]
        for i in tokens:
            if i not in list1:
                stack1.append(int(i))
            else:
                first_number,second_number = stack1.pop(), stack1.pop()
                if i == "+":
                    stack1.append(second_number + first_number)
                elif i == "-":
                    stack1.append(second_number - first_number)
                elif i == "*":
                    stack1.append(second_number * first_number)
                else: 
                    stack1.append(int(second_number / first_number))
        return stack1[0]

        
                    
                
        