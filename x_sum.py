x = int(input())
for i in  range(x):
    n,m = [int(j) for j in input().split()]
    
    grid = []
    for i in range(n):
        arr = [int(j) for j in input().split()]
        grid.append(arr)
        
    
    def in_bound(row,col):
        return 0 <= row < n and 0 <= col < m
    
    def find_sum(grid,row,col):
        
        sum =  grid[row][col]
        t_row = row + 1
        t_col = col + 1
        while in_bound(t_row,t_col):
            sum += grid[t_row][t_col]
            t_row += 1
            t_col += 1
            
        t_row = row + 1
        t_col = col - 1
        while in_bound(t_row,t_col):
            sum += grid[t_row][t_col]
            t_row += 1
            t_col -= 1
            
        t_row = row - 1
        t_col = col + 1
        while in_bound(t_row,t_col):
            sum += grid[t_row][t_col]
            t_row -= 1
            t_col += 1
        
        t_row = row - 1
        t_col = col - 1
        while in_bound(t_row,t_col):
            sum += grid[t_row][t_col]
            t_row -= 1
            t_col -= 1
        return sum
        
        
    max_sum = 0
    for i in range(n):
        for j in range(m):
            temp = find_sum(grid,i,j)
            if temp > max_sum:
                max_sum = temp
    print(max_sum)
            
            
