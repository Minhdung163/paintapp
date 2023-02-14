from .settings import *

def init_grid(rows,cols,color): #Create the grid for your painting app
    grid = [] #Create the list
    for i in range(rows): #For loop to insert the values into the grid
        grid.append([]) #Insert rows
        for _ in range(cols):
            grid[i].append(color) #Insert cols with a color variable
    return grid #This function return a list with a form of matrix in it


 


