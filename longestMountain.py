class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        lenLongest = 0
        i = 0
        while i+1 < len(arr) :
            while i+1 < len(arr) and arr[i] == arr[i+1] :
                i += 1
            positive = 0
            negative = 0
            while i+1 < len(arr) and arr[i] < arr[i+1] :
                positive += 1
                i += 1
            while i+1 < len(arr) and arr[i] > arr[i+1] :
                negative += 1
                i += 1
            if positive > 0 and negative > 0 and positive + negative + 1 > lenLongest:
                lenLongest = positive + negative + 1
        return lenLongest
                
             