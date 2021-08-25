#Montako huonetta talossa on?


def count(r):
    #print(r)
    n = len(r)
    m = len(r[0])
    grid = []
    for i in range(n):
        s = []
        grid.append(s)   
        for j in range(m):
            if r[i][j] == "#":
                s.append(1)
            elif r[i][j] == ".":
                s.append(0)
   #print(grid)
    laskuri = 0

    for a in range(len(grid)):
        for b in range(len(grid)):
    
            if grid[a][b] == 0:
                laskuri += 1
                #print(b)
                #print(a)  
                dfs(grid, a, b)
        
    return laskuri
       
def dfs(grid, y, x):
    n = len(grid)
    if grid[y][x] == 1:
       
        return 
    grid[y][x] = 1
    dfs(grid,y-1, x)
    dfs(grid,y+1, x)
    dfs(grid,y, x-1)
    dfs(grid,y, x+1)

if __name__ == "__main__":
    r = ["########",
         "#..#...#",
         "####.#.#",
         "#..#.#.#",
         "########"]
    print(count(r)) # 3