class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        
        
        
        def smallest_counter(s):
            
            d = defaultdict(int)
            small_char = s[0]
            for ele in s:
                if ele < small_char :
                    small_char = ele
            return s.count(small_char)
        
        def binary_search(ans):
            
            left  = 0
            right = len(arr_word)
            
            while left < right :
                mid = left + (right-left)//2
                
                if arr_word[mid] > ans:
                    right = mid
                else:
                    left = mid + 1 
                    
            return  len(arr_word) - left
                
        arr_word = []
        arr_query = []
        
        for word in words:
            arr_word.append(smallest_counter(word))
        
        arr_word.sort()
        
        for query in queries:
            arr_query.append(smallest_counter(query))
        
        ans = []
        
        for val in arr_query:
            ans.append(binary_search(val))
        
        return ans
            
            
            
        
            
        
        
                    
            
            
            
        