from collections import defaultdict
graph = defaultdict(list)

def AddEdge(u,v):
    graph[u].append(v)
    graph[v].append(u)
    
def Vertex(u):
    for i in graph[u]:
        print(i,end=" ")
    print()

n = int(input())
size = int(input())

for i in range(size):
    temp = [int(j) for j in input().split()]
    if temp[0] == 1:
        AddEdge(temp[1], temp[2])
    else:
        Vertex(temp[1])
