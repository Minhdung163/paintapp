from utils import * #Import everything from utils folder

WIN = pygame.display.set_mode((WIDTH,HEIGHT)) #Create the window with given width and height from the settings
pygame.display.set_caption("Paint") #And set the caption for it

def init_grid(rows,cols,color): #Create the grid for your painting app
    grid = [] #Create the list
    for i in range(rows): #For loop to insert the values into the grid
        grid.append([]) #Insert rows
        for _ in range(cols):
            grid[i].append(color) #Insert cols with a color variable
    return grid #This function return a list with a form of matrix in it

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

def get_row_col_from_pos(pos): #Get the pos of the mouse function
    x, y = pos
    row = y // PIXEL_SIZE #This rounds the position the match the index of the grid
    col = x // PIXEL_SIZE
    if row >= ROWS:
        raise IndexError #An exception in python occurs when we try to access an out-of-range element from a list so that we can detect when we click outside of the grid's area 
    return row, col

run = True
clock = pygame.time.Clock()
grid = init_grid(ROWS,COLS,BG_COLOR) #Create the grid with given rows, cols, and color from the settings
drawing_color = BLACK 
# Positions y to place to buttons
button_y1 =HEIGHT - TOOLBAR_HEIGHT*3/4 - 25 
button_y2 = HEIGHT - TOOLBAR_HEIGHT/4 - 25
buttons = [
    Button(10, button_y1, 50, 50, BLACK),
    Button(120, button_y1, 50, 50, RED),
    Button(230, button_y1, 50, 50, GREEN),
    Button(340, button_y1, 50, 50, BLUE),
    Button(450, button_y1, 50, 50, WHITE, "Erase", BLACK),
    Button(560, button_y1, 50, 50, WHITE, "Clear", BLACK),
    Button(10, button_y2, 50, 50, WHITE, "1px", BLACK),
    Button(120, button_y2, 50, 50, WHITE, "3px", BLACK),
    Button(230, button_y2, 50, 50, WHITE, "5px", BLACK),
    Button(340, button_y2, 50, 50, WHITE, "7px", BLACK),
    Button(450, button_y2, 50, 50, WHITE, "9px", BLACK)   
]# Initialize the buttons
while run: # while loop for the game
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT: #Close the game 
            run =False
        if pygame.mouse.get_pressed()[0]: # Check the event if you left-clicked the mouse
            pos = pygame.mouse.get_pos() # Return the current pos of the mouse
            try:
                row, col = get_row_col_from_pos(pos) # Return the row and col of grid at the area the mouse is pointing at
                if CHOOSE_SIZE == 1:                 # Fill the row and col of the grid with chosen color and chosen size of the brush
                    grid[row][col] = drawing_color
                if CHOOSE_SIZE == 2:
                    grid[row][col-1] = drawing_color
                    grid[row][col] = drawing_color
                    grid[row][col+1] = drawing_color
                if CHOOSE_SIZE == 3:
                    grid[row][col-2] = drawing_color
                    grid[row][col-1] = drawing_color
                    grid[row][col] = drawing_color
                    grid[row][col+1] = drawing_color
                    grid[row][col+2] = drawing_color
                if CHOOSE_SIZE == 4:
                    grid[row][col-3] = drawing_color
                    grid[row][col-2] = drawing_color
                    grid[row][col-1] = drawing_color
                    grid[row][col] = drawing_color
                    grid[row][col+1] = drawing_color
                    grid[row][col+2] = drawing_color
                    grid[row][col+3] = drawing_color
                if CHOOSE_SIZE == 5:
                    grid[row][col-4] = drawing_color
                    grid[row][col-3] = drawing_color
                    grid[row][col-2] = drawing_color
                    grid[row][col-1] = drawing_color
                    grid[row][col] = drawing_color
                    grid[row][col+1] = drawing_color
                    grid[row][col+2] = drawing_color
                    grid[row][col+3] = drawing_color
                    grid[row][col+4] = drawing_color
            except IndexError: # Exception when you clicked outside of the drawable area
                for button in buttons: # For loop to run through all of the buttons created
                    if not button.clicked(pos): # Ignore all the command other than left-click
                        continue
                    drawing_color = button.color # The drawing_color is equal to the color of clicked button
                    if button.text == "Clear": # Clear button turns all of the pixels in the grid into color white
                        grid = init_grid(ROWS, COLS, BG_COLOR)
                        drawing_color = BLACK  # After the clearance return the color and the brush size to default
                        CHOOSE_SIZE = 1
                    if button.text == None or button.text == "Erase": # Return the bool of each color so that we can change the brush'es size later on                    
                        if button.color == BLACK:
                            IS_BLACK = True
                            IS_RED = False
                            IS_GREEN = False
                            IS_BLUE = False
                            IS_WHITE = False
                        if button.color == RED:
                            IS_BLACK = False
                            IS_RED = True
                            IS_GREEN = False
                            IS_BLUE = False
                            IS_WHITE = False
                        if button.color == GREEN:
                            IS_BLACK = False
                            IS_RED = False
                            IS_GREEN = True
                            IS_BLUE = False
                            IS_WHITE = False
                        if button.color == BLUE:
                            IS_BLACK = False
                            IS_RED = False
                            IS_GREEN = False
                            IS_BLUE = True
                            IS_WHITE = False
                        if button.color == WHITE:
                            IS_BLACK = False
                            IS_RED = False
                            IS_GREEN = False
                            IS_BLUE = False
                            IS_WHITE = True                   
                    if button.text == "1px": # As we click the "1px" button, the brush still has the latest chosen color and set the brush size to 1 px
                        CHOOSE_SIZE = 1
                        if IS_BLACK:
                            drawing_color = BLACK
                        elif IS_WHITE:
                            drawing_color = WHITE
                        elif IS_BLUE:
                            drawing_color = BLUE
                        elif IS_GREEN:
                            drawing_color = GREEN
                        elif IS_RED:
                            drawing_color = RED                               
                    elif button.text == "3px": # Same logic applies to other cases
                        CHOOSE_SIZE = 2
                        if IS_BLACK:
                            drawing_color = BLACK
                        elif IS_WHITE:
                            drawing_color = WHITE
                        elif IS_BLUE:
                            drawing_color = BLUE
                        elif IS_GREEN:
                            drawing_color = GREEN
                        elif IS_RED:
                            drawing_color = RED                                   
                    elif button.text == "5px":
                        CHOOSE_SIZE = 3
                        if IS_BLACK:
                            drawing_color = BLACK
                        elif IS_WHITE:
                            drawing_color = WHITE
                        elif IS_BLUE:
                            drawing_color = BLUE
                        elif IS_GREEN:
                            drawing_color = GREEN
                        elif IS_RED:
                            drawing_color = RED                               
                    elif button.text == "7px":
                        CHOOSE_SIZE = 4
                        if IS_BLACK:
                            drawing_color = BLACK
                        elif IS_WHITE:
                            drawing_color = WHITE
                        elif IS_BLUE:
                            drawing_color = BLUE
                        elif IS_GREEN:
                            drawing_color = GREEN
                        elif IS_RED:
                            drawing_color = RED                               
                    elif button.text == "9px":
                        CHOOSE_SIZE = 5
                        if IS_BLACK:
                           drawing_color = BLACK
                        elif IS_WHITE:
                           drawing_color = WHITE
                        elif IS_BLUE:
                           drawing_color = BLUE
                        elif IS_GREEN:
                           drawing_color = GREEN
                        elif IS_RED:
                           drawing_color = RED
    draw(WIN, grid,buttons) # Use the draw function above in while loop with the parameters we have created

pygame.quit() # End of while loop and quit the game