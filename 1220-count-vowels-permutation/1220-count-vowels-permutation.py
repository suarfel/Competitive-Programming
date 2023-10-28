class Solution:
    def countVowelPermutation(self, n: int) -> int:
        
        
        # A  hashmap which holds a vowel followers 
        
        vowel_map = defaultdict(set)
        vowel_map['a'] = {'e'}
        vowel_map['e'] = {'a','i'}
        vowel_map['i'] = {'a','e','o','u'}
        vowel_map['o'] = {'i','u'}
        vowel_map['u'] = {'a'}
        
        @lru_cache(None)
        def dp(char,n):
            
            if n == 1:
                return 1
            
            ans = 0
            for vowel in vowel_map:
                if vowel in vowel_map[char]:
                    ans += dp(vowel,n-1)
            return ans
        
        ans = 0
        for letter in vowel_map:
            ans += dp(letter,n)
        return ans% (pow(10,9) + 7)
        
        
        
        