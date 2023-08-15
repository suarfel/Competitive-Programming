n = int(input())
for i in range(n):
    x = int(input())
    temp = []
    li = [int(j) for j in input().split()]
    for val in li:
        if not temp:
            temp.append(val)
        else:
            if temp[-1] < 0 and val < 0:
                temp[-1] = max(temp[-1],val)
            elif temp[-1] > 0 and val > 0 :
                temp[-1] = max(temp[-1],val)
            else:
                temp.append(val)
    print(sum(temp))
