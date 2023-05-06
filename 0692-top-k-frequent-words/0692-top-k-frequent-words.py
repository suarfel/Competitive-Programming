class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        
        counter = {}
        for word in words:
            if word in counter:
                counter[word] += 1
            else:
                counter[word] = 1
        heap = [(counter[word],word) for word in counter]
        
        heapq.heapify(heap)
        
        
        temp = []
        while len(heap) != k:
            temp.append(heapq.heappop(heap))
        ans = []
        for i in range(k):
            ans =  [heapq.heappop(heap)[1]] + ans
        
        
        
        for word in temp:
            if counter[word[1]] == counter[ans[-1]]:
                ans.append(word[1])
                
        
        print(ans)
        for i in range(len(ans)):
            j = len(ans) - 1
            while j > 0:
                if counter[ans[j]] == counter[ans[j-1]] :
                    if ans[j] < ans[j-1]:
                        ans[j],ans[j-1] = ans[j-1],ans[j]

                j -= 1


        return ans[0:k]
        
            
            
        
        