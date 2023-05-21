n = int(input())
for i in range(n):
    m = int(input())
    l = [int(j) for j in input().split()]
    l.sort()
    temp = 'YES'
    for j in range(len(l)-1):
        if abs(l[j]-l[j+1]) > 1 :
            temp = 'NO'
            
    print(temp)
    
