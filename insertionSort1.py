def insertionSort1(n, arr):
    temp = arr[-1]
    for i in range(n-2,-1,-1):
        if temp > arr[i]:
            arr[i+1] = temp
            for j in arr:
                print(j,end= " ")
            break
        else:
            arr[i+1] = arr[i]
            for j in arr:
                print(j,end=" ")
            print()
        if i==0 and temp < arr[i]:
            arr[i+1] = arr[i]
            arr[i] = temp
            for j in arr:
                print(j,end=" ")