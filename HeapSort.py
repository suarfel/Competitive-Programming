class Solution:
    #Heapify function to maintain heap property.
    def heapify(self,arr, n, i):
        
        small = i
        left = 2 * i + 1
        right = 2 * i + 2
        
        if left < n and arr[left] < arr[small]:
            small = left
            
        if right < n and arr[right] < arr[small]:
            small = right
        
        if small != i:
            arr[small],arr[i] = arr[i],arr[small]
            self.heapify(arr,n,small)
            
        return arr
        # code here
    
    #Function to build a Heap from array.
    def buildHeap(self,arr,n):
        heapq.heapify(arr)
        return arr
        # code here
    
    #Function to sort an array using Heap Sort.    
    def HeapSort(self, arr, n):
        arr = self.buildHeap(arr,n)
        i = len(arr) - 1
        j = 0
        while i > j:
            
            arr[i],arr[j] = arr[j],arr[i]
            n = n -1
            self.heapify(arr,n,j)
            i -= 1
        return arr.reverse()
