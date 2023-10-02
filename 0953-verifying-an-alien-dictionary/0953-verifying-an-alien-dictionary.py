class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        
        order_dict = {}
        
        for i in range(26):
            order_dict[order[i]] = i
        
        for i in range(len(words)):
            for j in range(i+1,len(words)):
                k = 0
                while k < len(words[i]) or k < len(words[j]) :
                    
                    if k < len(words[i]) and k < len(words[j]):
                        
                        if order_dict[words[i][k]] < order_dict[words[j][k]]:
                            break
                        elif  order_dict[words[i][k]] == order_dict[words[j][k]]:
                            k += 1
                        else:
                            return False
                    
                    elif k < len(words[i]):
                        return False
                    else:
                        break
        return True
                    
                
                
        