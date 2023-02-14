from utils import *

def draw_grid(win, grid): #Function to draw the grid as we've already created a grid
    for i, row in enumerate(grid): #for loop using enumerate, which gives you back 2 variables: i for count and row stands for what is inside that index
        for j, pixel in enumerate(row): 
            pygame.draw.rect(win, pixel, (j * PIXEL_SIZE, i * PIXEL_SIZE, PIXEL_SIZE, PIXEL_SIZE)) #Draw a square with each pixels in the grid

    if DRAW_GRID_LINES: #using bool data type to decides whether you want to draw grid lines or not 
        for i in range(ROWS + 1): #Add one more line to look good
            pygame.draw.line(win, BLACK,(0,i*PIXEL_SIZE),(WIDTH,i*PIXEL_SIZE)) #Draw the grid lines vertically
        for i in range(COLS + 1): 
            pygame.draw.line(win, BLACK,(i*PIXEL_SIZE,0),(i*PIXEL_SIZE,HEIGHT - TOOLBAR_HEIGHT)) #Draw the grid lines horizontally


def draw(win, grid, buttons): #Draw function
    win.fill(BG_COLOR)
    draw_grid(win, grid)
    for button in buttons: #For loop to draw all of the buttons 
        button.draw(win)
    pygame.display.update()




