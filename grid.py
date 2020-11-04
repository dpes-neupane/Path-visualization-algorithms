import pygame as py
import time
#window size 
WINDOW_WIDTH = 1202
WINDOW_HEIGHT = 685
#simple color
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
light_green = (104, 255, 104)
red_light = (255, 50, 50)




#intialize pygame
py.init()
key = None
py.display.set_caption("PATH ALGORITHMS")
myfont = py.font.SysFont('Comic Sans MS', 30) 
smallfont = py.font.SysFont('Comic Sans MS', 20)   
screen = py.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = py.time.Clock()



class Grid:
    

    def __init__(self,rows, cols, window, width, height):
        self.rows = rows
        self.cols = cols
        self.window = window
        self.width = width
        self.height = height
        self.selected = None

        self.x = 0
        self.y = 0
        self.dif = self.width / self.cols
    def get_cord(self,pos):
        #get position of the mouse when clicked in the box

        click_x = pos[0] // self.dif
       
        click_y = pos[1] // self.dif
        return (click_x, click_y)

    def draw(self):
        #the grid is drawn 
        self.window.fill((20, 100, 50))
        for i in range((self.rows+1)):
            
            py.draw.line(self.window, (255, 255, 255), (self.x, i * self.dif ), (self.width, i * self.dif), 1)
            py.draw.line(self.window, (244, 244, 244), (i * self.dif, self.y), (i * self.dif, self.height-5), 1)
    
    
    
    def select_start(self, row, col):
        
        py.draw.rect(self.window, (255, 0, 0), (row * self.dif, col * self.dif, self.dif, self.dif))

    def select_end(self, row, col):
        py.draw.rect(self.window, (255, 153, 153), (row * self.dif, col * self.dif, self.dif, self.dif) )









#button function 
#x=top-left corner of the rectangle x-coordinate
#y=top-left corner of the rectangle y-coordinate
#w=width of the rectangle
#h=height of the rectangle
#ic=inactive button color
#ac=if button is pressed
def button (msg, x, y, w, h, ic, ac, action=None):
    mouse = py.mouse.get_pos()
    click = py.mouse.get_pressed()
    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        py.draw.rect(screen, ac, (x, y, w, h))
        if click[0] == 1 and action != None:
            action()
        
    else:
        py.draw.rect(screen, ic, (x, y, w, h))
    
    smallText = smallfont.render(msg, True, black)
    textRect = smallText.get_rect()
    textRect.center = ( (x+(w/2)), (y+(h/2)) )
    screen.blit(smallText, textRect) 
   


def intro():
    intro = True
    

    while True:
        for event in py.event.get():
            
            if event.type == py.QUIT:
                py.quit()
                quit()
            
                
        screen.fill((200, 100, 50))
        textSurface = myfont.render("Path algorithms", True, white )
        textRect = textSurface.get_rect()
        textRect.center = (WINDOW_WIDTH/2), (WINDOW_HEIGHT/16)
        screen.blit(textSurface, textRect)
        
        smalltext = smallfont.render("double press mouse to continue", True, black)
        smaltextRect = smalltext.get_rect()        
        smaltextRect.center = (WINDOW_WIDTH/2), (WINDOW_HEIGHT-30)
        screen.blit(smalltext, smaltextRect)       
        
        
        button("DFS", 250, 450, 100, 50, green, light_green, loop)#the main loop starts from here
        
        
        py.display.update()
        clock.tick(15)
        

#start function



def loop():
    
    gridSurface = py.Surface((1201, 600))
    
    
    grid = Grid(100, 100, gridSurface, 1201, 613 )
    
    run = True
    end = False
    start = False
    while run:
        
        clicked = None
        
        grid.draw()
        screen.fill(white)
        button("Start position", 100, 610, 200, 50, red, red_light)
        
        button("End position", 800, 610, 200, 50, red, red_light)
        for event in py.event.get():
            if event.type == py.QUIT:
                run = False
            if event.type == py.MOUSEBUTTONDOWN:
                pos = py.mouse.get_pos()
                clicked = grid.get_cord(pos)
                
                
        
        
                
        
        
        if clicked:
            print(pos)
            if (100 + 200) > pos[0] > 100 and (610 + 50) > pos[1] > 610:
                start = True
                end = False
            if (800 + 200) > pos[0] > 800 and (610 + 50) > pos[1] > 610:
                start = False
                end = True
            print(start)
            
            if start:
                grid.select_start(clicked[0], clicked[1])
                screen.blit(gridSurface, (0, 0)) 
                py.display.update()  
            elif end:
                grid.select_end(clicked[0], clicked[1]) 
                screen.blit(gridSurface, (0, 0)) 
                py.display.update()    
            else:
                screen.blit(gridSurface, (0, 0)) 
                py.display.update()     
                    
        
        
        
        
                
        clock.tick(60)
    py.quit()
    quit()

if __name__ == "__main__":
    intro()    