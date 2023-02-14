import pygame
pygame.init()
pygame.font.init()

WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
BLUE = (0,255,0)
GREEN = (0,0,255)

FPS = 500 # Set the fps of the game, 

WIDTH = 800
HEIGHT = 1000

ROWS = COLS = 200

TOOLBAR_HEIGHT = HEIGHT - WIDTH

PIXEL_SIZE = WIDTH // COLS 

BG_COLOR = WHITE

DRAW_GRID_LINES = False # You can decide to show the grid lines or not here

CHOOSE_SIZE = 1 # Default brush size is 1px

IS_BLACK = True # Default color is black

IS_RED = False

IS_GREEN = False

IS_BLUE = False

IS_WHITE = False

def get_font(size):
    return pygame.font.SysFont("Helvetica", size)

def get_row_col_from_pos(pos): #Get the pos of the mouse function
    x, y = pos
    row = y // PIXEL_SIZE #This rounds the position the match the index of the grid
    col = x // PIXEL_SIZE
    if row >= ROWS:
        raise IndexError #An exception in python occurs when we try to access an out-of-range element from a list so that we can detect when we click outside of the grid's area 
    return row, col

