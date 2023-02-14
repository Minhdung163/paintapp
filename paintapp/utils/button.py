from .settings import *

class Button: #Class contains everything we need for the buttons
    def __init__(self, x, y, width, height, color, text=None, text_color = BLACK):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.text = text
        self.text_color = text_color

    def draw(self,win): # Draw the buttons
        pygame.draw.rect(win, self.color, (self.x,self.y,self.width,self.height)) #Draw the rectangle
        pygame.draw.rect(win, BLACK, (self.x,self.y,self.width,self.height),2) #Draw the outline of the rectangle
        if self.text: # If the buttons contain text
            button_font = get_font(16)
            text_surface = button_font.render(self.text,True,self.text_color) #The True parameter stands for anti-aliasing, used to make the edges smoother
            win.blit(text_surface, (self.x + self.width/2 - text_surface.get_width()/2,self.y + self.height/2 - text_surface.get_height()/2)) 
            # Draw the texts on top of the rectangle and align it in the middle
    def clicked(self,pos): # This function checks if the mouse pos is in the buttons area or not
        x, y = pos
        # Return False with anything outside of the buttons' area
        if not (x >= self.x and x <= self.x + self.width):
            return False
        if not (y >= self.y and y <= self.y + self.height):
            return False

        return True