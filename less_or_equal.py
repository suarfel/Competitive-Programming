n,k = [int(i) for i in input().split()]
arr = [int(i) for i in input().split()]
arr.sort()
value = 0
if k == 0:
    if arr[0] != 1:
        print(1)
    else:
        print(-1)
elif k == len(arr):
    if arr[-1] <= pow(10,9):
        print(pow(10,9))
    else:
        print(-1)
else:
    for i in range(n-1):
        if k == i + 1:
            if arr[i] != arr[i+1]:
                value = arr[i]
                break
    if value == 0:
        print(-1)
    else:
        print(value)
    
        
        
