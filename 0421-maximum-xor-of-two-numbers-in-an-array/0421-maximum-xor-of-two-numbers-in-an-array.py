class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        
        self.root = {}
        length = len(bin(max(nums))[2:])
        arr = []
        
        
        for num in nums:
            bit = bin(num)[2:]
            if length > len(bit) :
                bit = "0"*(length-len(bit)) + bit
                
            arr.append(bit)
        
        for bit in arr:
            self.insert(bit)
        
        max_ = 0
        
        for num in arr:
            max_ = max(max_,self.search(num))
        
        return max_
            
    def insert(self,num):
        
        current = self.root
        
        for bit in num:
            
            if int(bit) not in current:
                current[int(bit)] = {}
            
            current = current[int(bit)]
            
    def search(self,num):
        ans = ''
        current = self.root
        d = {'0' : '1','1' : '0'}
        
        for bit in num:
            
            if int(d[bit]) in current  :
                ans += '1'
                current = current[int(d[bit])]
            else:
                ans += '0'
                current = current[int(bit)]
           
        return int(ans,2)
                
                
        
        