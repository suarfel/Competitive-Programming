n = int(input())
count_one = 0
count_two = 0
for i in range(n):
    temp = [int(i) for i in input().split()]
    for j  in range(len(temp)):
        if i == j and temp[j] == 1:
            count_one += 1
        elif temp[j] == 1:
            count_two += 1
print(count_one + count_two//2)
