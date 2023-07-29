n = int(input())
arr = [int(i) for i in input().split()]
count_odd = 0
count_even = 0
for i in arr:
    if i%2 != 0 :
        count_odd += 1
    else:
        count_even += 1
    if count_even > 0 and count_odd > 0:
        arr.sort()
        break
for i in arr: print(i,end=" ")
    

