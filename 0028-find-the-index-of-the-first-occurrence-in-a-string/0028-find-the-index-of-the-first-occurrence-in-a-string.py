class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        
        d_ = 27
        
        def hasher(word):
            total = 0
            n = len(word)
            for i in range(len(word)):
                total += (ord(word[i]) - ord('a') + 1) * d_**(n-1)
                n -= 1
            return total
        
        def add_last_poll_first(word,first,last):
            val = word - (ord(first) - ord('a') + 1)* d_**(len(needle)-1)
            val = val*d_ + (ord(last) - ord('a') + 1)
            return val
        
        if len(needle) > len(haystack):
            return -1
        
        i = 0
        j = len(needle)
        
        needle_hash = hasher(needle)
        start = haystack[i:j]
        haystack_hash = hasher(start)
        if needle_hash == haystack_hash:
            return 0
        
         
        while i < len(haystack) and j < len(haystack):
            haystack_hash = add_last_poll_first(haystack_hash,haystack[i],haystack[j])
            i += 1
            j += 1
            if needle_hash == haystack_hash :
                return i
        return -1
            
            
             
                

                
                