from collections import defaultdict 
n = int(input())

matrix = []

graph = defaultdict(list)


for i in range(n):
    arr = [int(j) for  j in input().split()]
    matrix.append(arr)
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if matrix[i][j] == 1:
            graph[i+1].append( j+1)
for i in graph:
    print(len(graph[i]),end=" ")
    for j in graph[i]:
        print(j,end=" ")
    print()
