class Solution: 
    def select(self, arr, i):
        temp=i
        for k in range(i+1,len(arr)):
            if arr[k] < arr[temp]:
                temp=k
        arr[i],arr[temp]=arr[temp],arr[i]
        return arr[i]
        
    
    def selectionSort(self, arr,n):
        for i in range(n):
            arr[i]=self.select(arr,i)
        return arr