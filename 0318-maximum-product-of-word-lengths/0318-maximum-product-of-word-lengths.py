class Solution:
    def maxProduct(self, words: List[str]) -> int:
        total_max = 0
        word_set = []
        for i in words:
            word_set.append(set(i))
        for i in range(len(words)):
            for j in range(i+1,len(words)):
                if len(word_set[i]) + len(word_set[j]) == len(word_set[i].union(word_set[j])):
                    if  len(words[i]) * len(words[j]) > total_max:
                        total_max = len(words[i]) * len(words[j])
        return total_max
                            
                
        