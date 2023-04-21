class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        arr = []
        ans = []
        for i in words:
            d = {}
            for j in i:
                if j in d:
                    d[j] += 1
                else:
                    d[j] = 1
                    
            arr.append(d)

        for x in arr[0]:
            for i in range(1,len(arr)):
                if x in arr[i]:
                    if arr[0][x] > arr[i][x]:
                        arr[0][x] = arr[i][x]
                else:
                    arr[0][x] = 0
                        
        for i in arr[0]:
            for j in range(arr[0][i]):
                ans.append(i)
                        
        return ans
        