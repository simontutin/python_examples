import numpy as np

board = """
031004700
649200080
027610409
962078000
005009603
300500000
090800010
018005030
753000024"""

board = """
400000805
030000000
000700000
020000060
000080400
000010000
000603070
500200000
104000000"""


# %%
def grid_from_string( sudoku_numbers ):
    grid = np.array([[int(i) for i in line] for line in sudoku_numbers.split()])
    return grid


# %%
def check_sudoku(grid):
    """ Return True if grid is a valid Sudoku square, otherwise False. """
    for i in range(9):
        # j, k index top left hand corner of each 3x3 tile
        j, k = (i // 3) * 3, (i % 3) * 3
        print("i is ", i)
        if len(set(grid[i,:])) != 9 or len(set(grid[:,i])) != 9                   or len(set(grid[j:j+3, k:k+3].ravel())) != 9:
            return False
    return True


# %%
# Turn the provided string, sudoku, into an integer array
grid = grid_from_string( board )
print(grid)

if check_sudoku(grid):
    print('grid valid')
else:
    print('grid invalid')


# %%
def display(grid):
    sep = " "
    cross = " + "
    vbar = "| "
    xbar = "-"*12
    line = "  "
    print(line)
    for i in range(9):
        if i in (3,6):
            print("--------+-------+--------")
        line = vbar
        for j in range(9):
            line += str(grid[i,j]) + sep
            if j in (2,5):
                line += vbar
        
        line += vbar
        print( line )


# %%
def solve(grid):

    count = 0
    for i in range(9):
        for j in range(9):
            
            if grid[i,j] == 0:     
                for n in possible_vals( i, j, grid ):
                    grid[i,j] = n
                    solve(grid)
                    grid[i,j] = 0                
                return 

    display( grid )
    print("")
     


def possible( r, c, n, grid ):
    
    print(grid[r,:])
    if n in grid[r,:]:
        return False 
    elif n in grid[:,c]:
        return False
    elif n in smallgrid( r,c,grid):
        return False 
    else:
        return True 

def smallgrid( r, c, grid ):
    rr = r//3*3
    cc = c//3*3

    return grid[rr:rr+3, cc:cc+3]

              
get_ipython().run_line_magic('time', 'solve( grid_from_string(board2))')


# %%
def possible_vals( r, c, grid):
    possibles = np.arange(1,10)
    
    rr = grid[r,:]
    cc = grid[:, c]
    sg = smallgrid(r,c,grid)

    vals = np.concatenate( (rr,cc,sg), axis=None) 

    poss = np.setdiff1d( possibles, vals )
   

    return poss 

possible_vals( 1,1,grid)


# %%
board2 = """
600030750
020040016
000072000
000010003
180060024
000900065
700004001
000000040
400157038"""

get_ipython().run_line_magic('time', 'solve( grid_from_string(board2))')


# %%
board3= """
080000090
070060210
006048700
800000530
020000000
163000000
000401900
000000070
209700005"""

solve( grid_from_string( board3 ))


# %%
get_ipython().run_line_magic('time', '')
board4 = """
080700300
069800000
000100204
010004002
000057030
800600000
340060000
000000760
000000010"""

get_ipython().run_line_magic('time', 'solve( grid_from_string(board4))')

