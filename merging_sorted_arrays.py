n,m = [int(i) for i in input().split()]
first_list =  [int(i) for i in input().split()]
second_list = [int(i) for i in input().split()]
i,j = 0,0
ans = []

while i < len(first_list) or j < len(second_list):
    if i < len(first_list) and j < len(second_list):
        if first_list[i] > second_list[j]:
            ans.append(second_list[j])
            j += 1
        else:
            ans.append(first_list[i])
            i += 1
    elif i < len(first_list) :
        ans.append(first_list[i])
        i += 1
    else:
        ans.append(second_list[j])
        j += 1
for i in ans:
    print(i,end=" ")
            
        
