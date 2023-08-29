class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        
        ans = []
        arr = []
        
        def form_ip(ip_arr):
            ip_ans = ""
            for ele in ip_arr:
                ip_ans = ip_ans + ele + '.' 
            ans.append(ip_ans[:len(ip_ans)-1])
                
        def back_track(start):
            
            if len(arr) == 4 :
                temp = ''.join(arr)
                if len(temp) == len(s):
                    form_ip(arr)
                return
            
            for i in range(start,len(s)):
                if (s[start:i+1][0] != '0' and int(s[start:i+1]) <= 255) or (s[start:i+1][0] == '0' and len(s[start:i+1]) == 1) :
                    arr.append(s[start:i+1])
                    back_track(i+1)
                    arr.pop()
        
        back_track(0)
        return ans
                
                