def func(grid):
    v=[[False for i in range(len(grid[0]))]  for j in range(len(grid))]
    count=0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 1 and not v[i][j]:
                func2(grid, v,i,j)
                count+=1                
    return count
                
def func2(grid, v,i,j):
    v[i][j]=True
    for h in range(-1,2):
        for a in range(-1,2):
            new_i=i+h
            new_j=j+a
            if 0<=new_i<len(grid) and 0<= new_j < len(grid[0]) and grid[new_i] [new_j]==1:
                func2(grid,v,new_i,new_j)
grid=[[0,1],[1,0],[1,1],[1,0]] 
i_count=func(grid)  
print(i_count) 
grid=[[0,1,1,1,0,0,0],[0,0,1,1,0,1,0]]   
i_count=func(grid)  
print(i_count)     