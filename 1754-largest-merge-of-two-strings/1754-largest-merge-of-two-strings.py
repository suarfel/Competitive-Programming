class Solution:
    def largestMerge(self, word1: str, word2: str) -> str:
        
        merge = ""
        i , j = 0, 0
        temp_one = i
        temp_two = j
        word1 += '.'
        word2 += '/'
        
        while  temp_one < len(word1) and temp_two < len(word2):
            if word1[temp_one] == word2[temp_two]:
                temp_one += 1
                temp_two += 1
            elif word1[temp_one] > word2[temp_two]:
                merge += word1[i]
                i += 1
                temp_one = i
                temp_two = j
            else:
                merge += word2[j]
                j += 1
                temp_two = j
                temp_one = i
                
            if temp_one >= len(word1):
                temp_one = i
            elif temp_two >= len(word2):
                temp_two = j
        
        if i < len(word1):
            merge += word1[i : len(word1)]
        if j < len(word2):
            merge += word2[j : len(word2)]
        
        return merge[0:len(merge)-2]
                
                
            
            
        
        