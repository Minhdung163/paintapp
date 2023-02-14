from utils import * #Import everything from utils folder
from drawing import *

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