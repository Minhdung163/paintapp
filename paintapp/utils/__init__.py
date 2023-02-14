from .settings import *
from .button import Button
from .grid import *
import pygame
pygame.init()
pygame.font.init()

WIN = pygame.display.set_mode((WIDTH,HEIGHT)) #Create the window with given width and height from the settings
pygame.display.set_caption("Paint") #And set the caption for it
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
