n,m = [int(i) for i in input().split()]
grid = []
for i in range(n):
    grid.append(input())

def checker(row,col):
    count = 0
    for letter in grid[row]:
        if letter == grid[row][col]:
            count += 1
    if count > 1:
        return False
    
    count = 0 
    for i in range(len(grid)):
        if grid[i][col] == grid[row][col]:
            count += 1
    if count > 1:
        return False
    
    return True
     
    
ans = ''
for  i in range(n):
    for j in range(m):
        if checker(i,j):
            ans += grid[i][j]
print(ans)
        
        
        
