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









class Grid:
    

    def __init__(self,rows, cols, window=None, width=None, height=None):
        self.rows = rows
        self.cols = cols
        self.window = window
        self.width = width
        self.height = height
        self.selected = None
        self.cubes = [[Cubes(i, j) for j in range(cols)] for i in range(rows)]
        self.x = 0
        self.y = 0
        if self.width is not None:
            self.dif = self.width // 100
        
        count = 0
        #making the grid as a graph with connections with each other when the grid is initialized
        for i in range(rows):
            for j in range(cols):
                
                self.cubes[i][j].make_values(count)
                count+=1
                
        for i in range(rows):
            for j in range(cols):
                if ( rows-1) > i > 0 and 0 < j < (cols-1):
                    self.cubes[i][j].make_connections(left=self.cubes[i][j-1], right=self.cubes[i][j+1], up=self.cubes[i-1][j], down=self.cubes[i+1][j])
            
                elif i == 0:
                    if j == 0:
                        self.cubes[i][j].make_connections(right=self.cubes[i][j+1], down=self.cubes[i+1][j] )
                    elif j == cols - 1:
                        self.cubes[i][j].make_connections(left=self.cubes[i][j-1], down=self.cubes[i+1][j] )
                    else:
                        self.cubes[i][j].make_connections(left=self.cubes[i][j-1], right=self.cubes[i][j+1], down=self.cubes[i+1][j] ) 
                elif i == (rows-1):
                    if j == 0:
                        self.cubes[i][j].make_connections(right=self.cubes[i][j+1], up=self.cubes[i-1][j] )  
                    elif j == cols - 1:
                        self.cubes[i][j].make_connections(left=self.cubes[i][j-1], up=self.cubes[i-1][j] )
                    else:
                        self.cubes[i][j].make_connections(left=self.cubes[i][j-1], right=self.cubes[i][j+1], up=self.cubes[i-1][j] ) 
                    
                else:
                    if j == 0:
                        self.cubes[i][j].make_connections(right=self.cubes[i][j+1], up=self.cubes[i-1][j], down=self.cubes[i+1][j] )
                    else:
                        self.cubes[i][j].make_connections(left=self.cubes[i][j-1], up=self.cubes[i-1][j], down=self.cubes[i+1][j] )
            
                    
        
        
        
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
        
        
        
        
    def get_cubes(self):
        return self.cubes
    
    
    
    

    

class Cubes:
    
    
    
    def __init__(self, row, column):
        self.row = row
        self.column = column
        self.value = None
        
    
    def make_values(self, value):
        self.value = value
    
    def make_connections(self, left=None, right=None, up=None, down=None):
        self.left = left
        self.right = right
        self.up = up
        self.down = down
    
    
    def value(self):
        return self.value 
        
    def print_row_col(self):
        return self.row, self.column   
        
    def show_connections(self):
        # print(f"row={self.row}, column={self.column}, right={self.right}, left={self.left}, up={self.up}, down={self.down}, value={self.value}")
        return [self.left, self.right, self.up, self.down]
    
        



#button function 
#x=top-left corner of the rectangle x-coordinate
#y=top-left corner of the rectangle y-coordinate
#w=width of the rectangle
#h=height of the rectangle
#ic=inactive button color
#ac=if button is pressed
def button (msg, x, y, w, h, ic, ac, action=None, parameters=None):
    mouse = py.mouse.get_pos()
    click = py.mouse.get_pressed()
    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        py.draw.rect(screen, ac, (x, y, w, h))
        if click[0] == 1 and action != None:
            if parameters:
                action(parameters)
            else:
                action()
        
    else:
        py.draw.rect(screen, ic, (x, y, w, h))
    
    smallText = smallfont.render(msg, True, black)
    textRect = smallText.get_rect()
    textRect.center = ( (x+(w/2)), (y+(h/2)) )
    screen.blit(smallText, textRect) 
   





#the path algorithms

def DFS_starter(window, s, e, rows, cols):
   

        
    visited = [False for i in range(rows*cols)]

    stack = []

    
    path = DFS(window, visited, s, e, stack)
    return path
    
    
def DFS(window, visited, s, e, stack):
    parentMap = {} #for storing the vertex parent -- where the path came from to that node
    stack.append(s)
    traversal = []
    while(len(stack)):
        s = stack[-1]
        stack.pop()
        
        
        if s.value== e.value:
            break
        
        
        if ( not visited[s.value]):        
            # print(s.value, end=" ")
            traversal.append(s)
            visited[s.value] = True
        for node in s.show_connections():
            if node:
                if ( not visited[node.value]):
                    stack.append(node)
                    parentMap[node] = s
            

    return parentMap, traversal






def refresh():
    dfs_loop()




def intro():
    
    

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
        
        
        
        
        
        button("BFS", 300, 450, 100, 50, green, light_green, )
        
        
        button("DFS", 150, 450, 100, 50, green, light_green, dfs_loop)
        
        py.display.update()
        clock.tick(15)
        



def dfs_loop():
    
    gridSurface = py.Surface((1201, 600))
    state = True
    rows = 100
    cols = 50
    grid = Grid(rows, cols, gridSurface, 1201, 600 )
    clicked = None
    run = True
    once = True
    complete_first_time = False
    end = False
    start = False
    find = False
    starting_position = None
    end_position = None
    
    
    
    while run:
        
        
        
        
        
            
        #drawing the grid
        grid.draw()
        screen.fill(white)
        
        
              
        button("Start position", 120, 610, 200, 50, red, red_light)
        
        button("End position", 850, 610, 200, 50, red, red_light)
        
        
        for event in py.event.get():
            if event.type == py.QUIT:
                run = False
            if event.type == py.MOUSEBUTTONDOWN:
                pos = py.mouse.get_pos()
                clicked = grid.get_cord(pos)
        
        
        
        
                
        
        if state: #pause button imitator
            # if some one of the button is clicked then the it performs the action related to it
            
            if clicked:
                print(clicked)
                if (100 + 200) > pos[0] > 100 and (610 + 50) > pos[1] > 610:
                    start = True
                    
                if (800 + 200) > pos[0] > 800 and (610 + 50) > pos[1] > 610:
                    start = False
                    end = True
                if end_position and starting_position:
                    if not once:
                        if (500 + 200) > pos[0] > 500 and (610 + 50) > pos[1] > 610:
                            find = True
                            end = False
                            
                
            if start: # if start is clicked then we can then select some box in the grid and it will be highlighted in red color
                    grid.select_start(clicked[0], clicked[1])
                    starting_position = clicked
                    screen.blit(gridSurface, (0, 0))
                    py.display.update()   
                        
            elif end: # likewise for the end position but in pink color
                    grid.select_end(clicked[0], clicked[1]) 
                    end_position = clicked
                    if starting_position:
                        grid.select_start(starting_position[0], starting_position[1])
                    
                            
                    button("Find path", 500, 610, 200, 59, red, red_light)
                    screen.blit(gridSurface, (0, 0))
                    py.display.update()  
            elif find: # the path finding occurs in here
                    cubes_ = grid.get_cubes()
                    
                    grid.select_start(starting_position[0], starting_position[1])
                    
                    diff = WINDOW_WIDTH // 100
                    # the function returns the dictionary of the path that it took to get the end position but is in reverse order and also the traversal path
                    path, traversal = DFS_starter( gridSurface, cubes_[ int( starting_position[0]  ) ]  [ int( starting_position[1] ) ]   , cubes_[ int( end_position[0] ) ]  [ int(end_position[1]) ], rows, cols)
                    for i in traversal: #shows the traversal
                        py.draw.rect(gridSurface, (255, 100, 100), (i.print_row_col()[0] * diff, i.print_row_col()[1] * diff, diff, diff), 1)
                    
                    screen.blit(gridSurface, (0, 0))
                    py.display.update()
                    # starting node
                    curr = cubes_[ int( end_position[0] ) ]  [ int(end_position[1]) ]
                    curr = path[curr]
                    grid.select_end(curr.print_row_col()[0], curr.print_row_col()[1])
                    # to highlight the path 
                    while curr != cubes_[ int( starting_position[0]  ) ]  [ int( starting_position[1]) ]:
                            
                            bo = py.draw.rect(gridSurface, (255, 0, 0), (curr.print_row_col()[0] * diff, curr.print_row_col()[1] * diff, diff, diff), 1)
                            if not complete_first_time:
                                screen.blit(gridSurface, (0, 0))
                                py.display.update(bo)
                                py.time.delay(3)
                                
                            curr = path[curr]
                    state = False # to pause the loop---kind of!
                    
                    
                    if not complete_first_time:  
                        complete_first_time = True
                        
                        screen.blit(gridSurface, (0, 0))
                        py.display.update()
        
        
        else:# same function but it just shows the same path but it will show all the path at once 
                    
            grid.select_start(starting_position[0], starting_position[1])
            
            curr = cubes_[ int( end_position[0] ) ]  [ int(end_position[1]) ]
            grid.select_end(curr.print_row_col()[0], curr.print_row_col()[1])
            curr = path[curr]
            diff = WINDOW_WIDTH // 100
            while curr != cubes_[ int( starting_position[0]  ) ]  [ int( starting_position[1]) ]:
                    
                    py.draw.rect(gridSurface, (255, 0, 100), (curr.print_row_col()[0] * diff, curr.print_row_col()[1] * diff, diff, diff), 1)
                    
                        
                    curr = path[curr]
            button("Refresh", 500, 610, 200, 59, red, red_light, refresh )
            
            screen.blit(gridSurface, (0, 0))               
            py.display.update()
                
                
                
                
                
                
        if once:
            once = False
            screen.blit(gridSurface, (0, 0))
            py.display.update()  
                 
        
         
        clock.tick(60)
    py.quit()
    quit()







if __name__ == "__main__":
    #intialize pygame
    py.init()
    key = None
    py.display.set_caption("PATH ALGORITHMS")
    myfont = py.font.SysFont('Comic Sans MS', 30) 
    smallfont = py.font.SysFont('Comic Sans MS', 20)   
    screen = py.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    clock = py.time.Clock()
    intro()    