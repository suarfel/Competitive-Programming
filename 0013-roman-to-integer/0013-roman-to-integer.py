class Solution:
    def romanToInt(self, s: str) -> int:
        integer_value = 0
        symbol_values = { "I" :1,"V":5 , "X" : 10,"L":50,"C" : 100,"D" : 500,"M":1000}
        for i in range(len(s)-1):
            print(i)
            print(i+1)
            if symbol_values[s[i]] >= symbol_values[s[i+1]]:
                integer_value += symbol_values[s[i]]
            else:
                integer_value -= symbol_values[s[i]]
        integer_value += symbol_values[s[-1]]
        return integer_value
            
            
        
        
        