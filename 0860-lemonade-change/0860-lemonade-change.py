class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        
        bill_five = 0
        bill_ten = 0
        for bill in bills:
            if bill == 5:
                bill_five += 1
            elif bill == 10 :
                if bill_five > 0:
                    bill_five -= 1
                    bill_ten += 1
                else:
                    return False
            else:
                if bill_five > 0 and bill_ten > 0:
                    bill_five -= 1
                    bill_ten -= 1
                elif bill_five > 2 :
                    bill_five -= 3
                    
                else:
                    return False
        return True
                    