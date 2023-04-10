n = int(input())
graph = []
sources = set()
sinks = set()
for i in range(n):
    l = [int(j) for j in input().split()]
    graph.append(l)

 
for i  in range(n):
    valid  = False
    valid_two = False
    for j in range(n):

        if graph[i][j] == 1:
            valid = True
        if graph[j][i] == 1:
            valid_two = True
        
    if not valid:
        sinks.add(i+1)
    if not valid_two:
        sources.add(i+1)
sources = list(sources)
sinks = list(sinks)

sources.sort()
sinks.sort()

print(len(sources),end=" ")
for i in sources:
    print(i,end=" ")
print()
print(len(sinks),end=" ")
for j in sinks:
    print(j,end=" ")
