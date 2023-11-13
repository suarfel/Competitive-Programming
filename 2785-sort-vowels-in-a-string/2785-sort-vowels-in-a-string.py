class Solution:
    def sortVowels(self, s: str) -> str:
        
        vowels = {'a','e','i','o','u','A','E','I','O','U'}
        vowels_idxs = []
        cur_vowels = []
        
        for idx,char in enumerate(s):
            if char in vowels:
                vowels_idxs.append(idx)
                cur_vowels.append(char)
        
        vowels_idxs.sort()
        cur_vowels = sorted(cur_vowels)
        
        s = list(s)
        for idx,ele in enumerate(vowels_idxs):
            s[ele] = cur_vowels[idx]
        
        return ''.join(s)
                
        