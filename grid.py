from queue import Queue, PriorityQueue
import pygame as py
import time
import math
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
            self.dif = self.width // cols
        
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
            py.draw.line(self.window, (244, 244, 244), (i * self.dif, self.y), (i * self.dif, self.height), 1)
    
    
    
    def select_start(self, row, col):#get starting position 
        py.draw.rect(self.window, (255, 0, 0), (row * self.dif, col * self.dif, self.dif, self.dif))
        
        
        

    def select_end(self, row, col):#get/draw end position
        py.draw.rect(self.window, (255, 153, 153), (row * self.dif, col * self.dif, self.dif, self.dif) )
        
        
        
        
    def get_cubes(self):
        return self.cubes
    
    
    def add_blocks(self, row, col):#method to add blocks to the path
        self.cubes[row][col].block_cell()
    
    def remove_blocks(self, row, col):#method to add blocks to the path
        self.cubes[row][col].unblock_cell()

    

class Cubes:
    
    
    
    def __init__(self, row, column):
        self.row = row
        self.column = column
        self.value = None
        self.blocked = False
    
    def make_values(self, value):#add value to each cube
        self.value = value
    
    def make_connections(self, left=None, right=None, up=None, down=None):#make the graph of each cube in the graph
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
    
    def block_cell(self):#turns the cube into a blocked cube
        self.blocked = True
    
    
    def unblock_cell(self):
        self.blocked = False
    
    
    def get_cell_condition(self):
        return self.blocked
        



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
   








#####################first menu loop########################




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
        
        
        
        
        
        button("BFS", 300, 450, 100, 50, green, light_green, BFS_loop )
        
        
        button("DFS", 150, 450, 100, 50, green, light_green, dfs_loop)
        
        button("Birdirectional", 500, 450, 150, 50, green, light_green, Bidirectional_loop)
        
        button("A Star", 700, 450, 100, 50, green, light_green, a_star_loop)
        
        py.display.update()
        clock.tick(15)
        
#####################menu loop ends here####################




##############################
############################
########################
########################
###BIDIRECTIONAL PATH ALGORITHM##########################



def Bidirectional_traversal( s, e, rows, cols):
    q = Queue()
    z = Queue()
    q.put(s)
    z.put(e)
    traversal = []
    traversal.append(s)
    traversal.append(e)
    parentMap_start = {}
    parentMap_end = {}
    visited_end = [False for i in range(rows * cols)]
    visited_start = [False for i in range(rows * cols)]
    visited_end[e.value] = True
    visited_start[s.value] = True
    flag = True
    intersection = None
    while not q.empty() and not z.empty():
        v = q.get()
        w = z.get()
        if not flag:
            break
        
        for node in v.show_connections():
            if node and not node.get_cell_condition():
                if not visited_start[node.value]:
                    
                    visited_start[node.value] = True
                    if visited_end[node.value]:
                        intersection = node
                        flag = False
                        
                    traversal.append(node)
                    # print(node.value)
                    q.put(node)
                    parentMap_start[node] = v
                
        if flag:     
            for node in w.show_connections():
                if node and not node.get_cell_condition():
                    if not visited_end[node.value]: 
                        
                        visited_end[node.value] = True
                        if visited_start[node.value]:
                            intersection = node
                            flag = False
                        traversal.append(node)
                        # print(node.value)
                        z.put(node)
                        parentMap_end[node] = w
                
                    
                
    return  (parentMap_start, parentMap_end), traversal, intersection




def Bidirectional_loop():
    gridSurface = py.Surface((601, 600))
    state = True
    rows = 50
    cols = 50
    grid = Grid(rows, cols, gridSurface, 601, 600 )
    clicked = None
    run = True
    once = True
    complete_first_time = False
    end = False
    start = False
    find = False
    starting_position = None
    end_position = None
    cubes_ = grid.get_cubes()
    make_wall = False
    del_wall = False
    diff = WINDOW_WIDTH // 100
    blocks = {}
    
    while run:
        
        
        
        
        
            
        #drawing the grid
        grid.draw()
        screen.fill(white)
        
        
              
        button("Start position", 50, 610, 135, 50, red, red_light)
        
        button("End position", 190, 610, 130, 50, red, red_light)
        
        button("Main Menu", 1070, 610, 110, 50, red, red_light, intro)
        button("Add blocks", 800, 610, 110, 50, red, red_light)
        button("Remove blocks", 920, 610, 140, 50, red, red_light)
        
        for event in py.event.get():
            if event.type == py.QUIT:
                run = False
            if event.type == py.MOUSEBUTTONDOWN:
                pos = py.mouse.get_pos()
                clicked = grid.get_cord(pos)
                
        
        
        
        
                
        
        if state: #pause button imitator
            
            # if one of the button is clicked then the it performs the action related to it
            if clicked:
                
                if (50 + 135) > pos[0] > 50 and (610 + 50) > pos[1] > 610:
                    start = True
                    
                if (190 + 130) > pos[0] > 190 and (610 + 50) > pos[1] > 610:
                    start = False
                    end = True
                if end_position and starting_position:
                    if not once:
                        if (500 + 200) > pos[0] > 500 and (610 + 50) > pos[1] > 610:
                            find = True
                            end = False
                if (800 + 110) > pos[0] > 800 and (610 + 50) > pos[1] > 610:
                    start = False
                    end = False
                    find = False
                    make_wall = True             
                if (920 + 140) > pos[0] > 920 and (610 + 50) > pos[1] > 610:
                    start = False
                    end = False
                    find = False
                    make_wall = False
                    del_wall = True 
                    
                
                
            if start: # if start is clicked then we can then select some box in the grid and it will be highlighted in red color
                if blocks: #showing the blocked boxes
                    for i in blocks.values():
                        py.draw.rect(gridSurface, (0, 0, 0), (i[0] * diff, i[1] * diff, diff, diff))
                grid.select_start(clicked[0], clicked[1])
                starting_position = clicked
                screen.blit(gridSurface, (0, 0))
                py.display.update()   
                        
            elif end: # likewise for the end position but in pink color
                if blocks: #showing the blocked boxes
                    for i in blocks.values():
                        py.draw.rect(gridSurface, (0, 0, 0), (i[0] * diff, i[1] * diff, diff, diff))
                grid.select_end(clicked[0], clicked[1]) 
                end_position = clicked
                if starting_position:
                    grid.select_start(starting_position[0], starting_position[1])
                    
                            
                button("Find path", 500, 610, 200, 59, red, red_light)
                screen.blit(gridSurface, (0, 0))
                py.display.update()  
            elif find: # the path finding occurs in here
                    
                    
                if (starting_position[0] < 50 and starting_position[1] <  50) and (end_position[0] < 50 and end_position[1] < 50):  
                    
                    if blocks: #showing the blocked boxes
                        for i in blocks.values():
                            py.draw.rect(gridSurface, (0, 0, 0), (i[0] * diff, i[1] * diff, diff, diff))
                    screen.blit(gridSurface, (0, 0))
                    py.display.update()
                    # the function returns the dictionary of the path that it took to get the end position but is in reverse order and also the traversal path
                    path, traversal, intersection = Bidirectional_traversal( cubes_[ int( starting_position[0]  ) ]  [ int( starting_position[1] ) ]   , cubes_[ int( end_position[0] ) ]  [ int(end_position[1]) ], rows, cols)
                    for i in traversal: #shows the traversal
                        b = py.draw.rect(screen, (255, 50, 100), (i.print_row_col()[0] * diff, i.print_row_col()[1] * diff, diff, diff), 1)
                        py.display.update(b)
                        py.time.delay(3)
                    grid.select_start(starting_position[0], starting_position[1])
                    grid.select_end(end_position[0], end_position[1])  
                    screen.blit(gridSurface, (0, 0))
                    py.display.update()
                    py.time.delay(10)
                
                    
                    # starting node
                    
                    
                    curr = path[0] [intersection]
                    
                    grid.select_end(curr.print_row_col()[0], curr.print_row_col()[1])
                    # to highlight the path 
                    
                    bo = py.draw.rect(gridSurface, (255, 0, 0), (intersection.print_row_col()[0] * diff, intersection.print_row_col()[1] * diff, diff, diff), 1)
                    py.display.update(bo)
                    while curr != cubes_[ int( starting_position[0]  ) ]  [ int( starting_position[1]) ]:
                            
                            bo = py.draw.rect(gridSurface, (255, 0, 0), (curr.print_row_col()[0] * diff, curr.print_row_col()[1] * diff, diff, diff), 1)
                            
                         
                            if not complete_first_time: 
                                
                                screen.blit(gridSurface, (0, 0))
                                py.display.update(bo)
                                py.time.delay(10)
                                    
                            curr = path[0] [curr]
                    
                    
                    
                    
                    
                    
                    curr = path[1] [intersection] 
                    
                    while curr != cubes_[ int( end_position[0]  ) ]  [ int( end_position[1]) ]:
                            
                            bo = py.draw.rect(gridSurface, (255, 0, 0), (curr.print_row_col()[0] * diff, curr.print_row_col()[1] * diff, diff, diff), 1)
                            
                            
                            
                            if not complete_first_time: 
                                
                                screen.blit(gridSurface, (0, 0))
                                py.display.update(bo)
                                py.time.delay(10)
                                    
                            curr = path[1] [curr]
                    
                    
                    state = False # to pause the loop---kind of!
                    
                    
                    if not complete_first_time:  
                        complete_first_time = True        
                        screen.blit(gridSurface, (0, 0))
                        py.display.update()
                
                else:
                    if (starting_position[0] > 50 or starting_position[1] >  50):
                        button("Please Select a Starting Position!", 602, 10, 400, 50, red, red)
                        screen.blit(gridSurface, (0, 0))
                        py.display.update()
                    elif (end_position[0] > 50 or end_position[1] >  50):
                        button("Please select an End Position!", 602, 0, 400, 50, red, red)
                        screen.blit(gridSurface, (0, 0))
                        py.display.update()
                    else:
                        button("Please select both Positions!", 602, 0, 400, 50, red, red)
                        screen.blit(gridSurface, (0, 0))
                        py.display.update()       
            
            
            elif make_wall:
                if (clicked[0] < 50 and clicked[1] <  50):  #to ensure that the clicked has tuple that is on the grid
                    bo = py.draw.rect(gridSurface, (0, 0, 0), (clicked[0] * diff, clicked[1] * diff, diff, diff))
                    
                    blocks[  cubes_[clicked[0]] [clicked[1]].value  ] = clicked
                    grid.add_blocks(clicked[0], clicked[1])
                    screen.blit(gridSurface, (0, 0))
                    py.display.update(bo)            
            elif del_wall:
                if (clicked[0] < 50 and clicked[1] <  50):  #to ensure that the clicked has tuple that is on the grid            
                    if blocks:
                        try:
                            del blocks[  cubes_[clicked[0]] [clicked[1]].value  ]
                            grid.remove_blocks(clicked[0], clicked[1])
                            for i in blocks.values():
                                py.draw.rect(gridSurface, (0, 0, 0), (i[0] * diff, i[1] * diff, diff, diff))
                            if starting_position and end_position:
                                button("Find path", 500, 610, 200, 59, red, red_light)
                                grid.select_start(starting_position[0], starting_position[1])
                                grid.select_end(end_position[0], end_position[1])
                            screen.blit(gridSurface, (0, 0))
                            py.display.update()
                        except Exception:
                            pass
                            

                        
                        
                        
                        
        else:# same function but it just shows the same path but it will show all the path at once 
            if blocks: #showing the blocked boxes
                for i in blocks.values():
                    py.draw.rect(gridSurface, (0, 0, 0), (i[0] * diff, i[1] * diff, diff, diff))
            grid.select_start(starting_position[0], starting_position[1])
            curr = cubes_[ int( end_position[0] ) ]  [ int(end_position[1]) ]
            grid.select_end(curr.print_row_col()[0], curr.print_row_col()[1])
            
                    
            curr = path[0] [intersection]
            
            
            # to highlight the path 
            bo = py.draw.rect(gridSurface, (255, 0, 0), (intersection.print_row_col()[0] * diff, intersection.print_row_col()[1] * diff, diff, diff), 1)
            py.display.update(bo)
            while curr != cubes_[ int( starting_position[0]  ) ]  [ int( starting_position[1]) ]:
                    
                    bo = py.draw.rect(gridSurface, (255, 0, 0), (curr.print_row_col()[0] * diff, curr.print_row_col()[1] * diff, diff, diff), 1)
                    
                    
                    
                    if not complete_first_time: 
                        
                        screen.blit(gridSurface, (0, 0))
                        py.display.update(bo)
                        py.time.delay(10)
                            
                    curr = path[0] [curr]
            
            
            
            
            
            
            curr = path[1] [intersection] 
            
            while curr != cubes_[ int( end_position[0]  ) ]  [ int( end_position[1]) ]:
                    
                    bo = py.draw.rect(gridSurface, (255, 0, 0), (curr.print_row_col()[0] * diff, curr.print_row_col()[1] * diff, diff, diff), 1)
                    
                    
                    
                    if not complete_first_time: 
                        
                        screen.blit(gridSurface, (0, 0))
                        py.display.update(bo)
                        py.time.delay(10)
                            
                    curr = path[1] [curr]
            
            
            state = False # to pause the loop---kind of!
            
            
            if not complete_first_time:  
                complete_first_time = True        
                screen.blit(gridSurface, (0, 0))
                py.display.update()
            
            
                    
                    
            button("Refresh", 500, 610, 200, 59, red, red_light, Bidirectional_loop )
            
            screen.blit(gridSurface, (0, 0))               
            py.display.update()
                
                
                
                
                
                
        if once:
            once = False
            screen.blit(gridSurface, (0, 0))
            py.display.update()  
                 
        
         
        clock.tick(60)
    py.quit()
    quit()

###############Bidirectional path visualization ends here################################






####      #######      ########      #############################################
#### #### ####### ############ ###################################################
####    #########    ###########   ###############################################
#### #### ####### ################# ##############################################
####     ######## ############     ###############################################




def BFS(s, e, visited, q):
    visited[s.value] = True
    traversal = []
    parentMap = {}
    q.put(s)
    traversal.append(s)
    
    while not q.empty():
        v = q.get()
        if v.value == e.value:
        
            break
        
        for node in v.show_connections():
            
            if node and not node.get_cell_condition():
                
                if not visited[node.value] :
                    visited[node.value] = True
                    traversal.append(node)
                    # print(node.value, node.print_row_col())
                    q.put(node)
                    parentMap[node] = v
        
    
    return parentMap, traversal




def BFS_starter(window, s, e, rows, cols):
    q = Queue()
    visited = [False for i in range(rows*cols)]        
    path = BFS(s, e, visited, q)
    return path








def BFS_loop():
    gridSurface = py.Surface((601, 600))
    state = True
    rows = 50
    cols = 50
    grid = Grid(rows, cols, gridSurface, 601, 600 )
    clicked = None
    run = True
    once = True
    complete_first_time = False
    end = False
    start = False
    find = False
    starting_position = None
    end_position = None
    make_wall = False
    diff = WINDOW_WIDTH // 100
    blocks = {}
    cubes_ = grid.get_cubes()
    del_wall = False
    
    while run:
        
        
        
        
        
            
        #drawing the grid
        grid.draw()
        screen.fill(white)
        
        
              
        button("Start position", 50, 610, 135, 50, red, red_light)
        
        button("End position", 190, 610, 130, 50, red, red_light)
        
        button("Main Menu", 1070, 610, 110, 50, red, red_light, intro)
        
        button("Add blocks", 800, 610, 110, 50, red, red_light)
        button("Remove blocks", 920, 610, 140, 50, red, red_light)
        
        for event in py.event.get():
            if event.type == py.QUIT:
                run = False
            if event.type == py.MOUSEBUTTONDOWN:
                pos = py.mouse.get_pos()
                clicked = grid.get_cord(pos)
                
        
        
        
        
                
        
        if state: #pause button imitator
            
            # if one of the button is clicked then the it performs the action related to it
            if clicked:
                
                if (50 + 135) > pos[0] > 50 and (610 + 50) > pos[1] > 610:
                    start = True
                    
                if (190 + 130) > pos[0] > 190 and (610 + 50) > pos[1] > 610:
                    start = False
                    end = True
                if end_position and starting_position:
                    if not once:
                        if (500 + 200) > pos[0] > 500 and (610 + 50) > pos[1] > 610:
                            find = True
                            end = False
                if (800 + 110) > pos[0] > 800 and (610 + 50) > pos[1] > 610:
                    start = False
                    end = False
                    find = False
                    make_wall = True    
                
                if (920 + 140) > pos[0] > 920 and (610 + 50) > pos[1] > 610:
                    start = False
                    end = False
                    find = False
                    make_wall = False
                    del_wall = True 
                
            if start: # if start is clicked then we can then select some box in the grid and it will be highlighted in red color
                if blocks: #showing the blocked boxes
                    for i in blocks.valuse():
                        py.draw.rect(gridSurface, (0, 0, 0), (i[0] * diff, i[1] * diff, diff, diff))
                grid.select_start(clicked[0], clicked[1])
                starting_position = clicked
                screen.blit(gridSurface, (0, 0))
                py.display.update()   
                        
            elif end: # likewise for the end position but in pink color
                if blocks: #showing the blocked boxes
                    for i in blocks.values():
                        py.draw.rect(gridSurface, (0, 0, 0), (i[0] * diff, i[1] * diff, diff, diff))
                grid.select_end(clicked[0], clicked[1]) 
                end_position = clicked
                if starting_position:
                    grid.select_start(starting_position[0], starting_position[1])
                    
                            
                button("Find path", 500, 610, 200, 59, red, red_light)
                screen.blit(gridSurface, (0, 0))
                py.display.update()  
            elif find: # the path finding occurs in here
                
                if (starting_position[0] < 50 and starting_position[1] <  50) and (end_position[0] < 50 and end_position[1] < 50):   
                    
                    
                    if blocks: #showing the blocked boxes
                        for i in blocks.values():
                            py.draw.rect(gridSurface, (0, 0, 0), (i[0] * diff, i[1] * diff, diff, diff))
                    # the function returns the dictionary of the path that it took to get the end position but is in reverse order and also the traversal path
                    path, traversal = BFS_starter( gridSurface, cubes_[ int( starting_position[0]  ) ]  [ int( starting_position[1] ) ]   , cubes_[ int( end_position[0] ) ]  [ int(end_position[1]) ], rows, cols)
                    for i in traversal: #shows the traversal
                        b = py.draw.rect(screen, (255, 50, 100), (i.print_row_col()[0] * diff, i.print_row_col()[1] * diff, diff, diff), 1)
                        py.display.update(b)
                        py.time.delay(3)
                    grid.select_start(starting_position[0], starting_position[1])
                    grid.select_end(end_position[0], end_position[1])  
                    screen.blit(gridSurface, (0, 0))
                    py.display.update()
                    py.time.delay(10)
                
                    
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
                                py.time.delay(10)
                                    
                            curr = path[curr]
                    state = False # to pause the loop---kind of!
                    
                    
                    if not complete_first_time:  
                        complete_first_time = True        
                        screen.blit(gridSurface, (0, 0))
                        py.display.update()
                else:
                    if (starting_position[0] > 50 or starting_position[1] >  50):
                        button("Please Select a Starting Position!", 602, 10, 400, 50, red, red)
                        screen.blit(gridSurface, (0, 0))
                        py.display.update()
                    elif (end_position[0] > 50 or end_position[1] >  50):
                        button("Please select an End Position!", 602, 0, 400, 50, red, red)
                        screen.blit(gridSurface, (0, 0))
                        py.display.update()
                    else:
                        button("Please select both Positions!", 602, 0, 400, 50, red, red)
                        screen.blit(gridSurface, (0, 0))
                        py.display.update()
            elif make_wall:
                if (clicked[0] < 50 and clicked[1] <  50):  #to ensure that the clicked has tuple that is on the grid
                    bo = py.draw.rect(gridSurface, (0, 0, 0), (clicked[0] * diff, clicked[1] * diff, diff, diff))
                    blocks[  cubes_[clicked[0]] [clicked[1]].value  ] = clicked
                    grid.add_blocks(clicked[0], clicked[1])
                    screen.blit(gridSurface, (0, 0))
                    py.display.update(bo)
            
            elif del_wall:
                if (clicked[0] < 50 and clicked[1] <  50):  #to ensure that the clicked has tuple that is on the grid            
                    if blocks:
                        try:
                            del blocks[  cubes_[clicked[0]] [clicked[1]].value  ]
                            grid.remove_blocks(clicked[0], clicked[1])
                            for i in blocks.values():
                                py.draw.rect(gridSurface, (0, 0, 0), (i[0] * diff, i[1] * diff, diff, diff))
                            if starting_position and end_position:
                                button("Find path", 500, 610, 200, 59, red, red_light)
                                grid.select_start(starting_position[0], starting_position[1])
                                grid.select_end(end_position[0], end_position[1])
                            screen.blit(gridSurface, (0, 0))
                            py.display.update()
                        except Exception:
                            pass



            
                        
        else:# same function but it just shows the same path but it will show all the path at once 
            
            if blocks: #showing the blocked boxes
                for i in blocks.values():
                    py.draw.rect(gridSurface, (0, 0, 0), (i[0] * diff, i[1] * diff, diff, diff))       
            grid.select_start(starting_position[0], starting_position[1])
            
            curr = cubes_[ int( end_position[0] ) ]  [ int(end_position[1]) ]
            grid.select_end(curr.print_row_col()[0], curr.print_row_col()[1])
            curr = path[curr]
            diff = WINDOW_WIDTH // 100
            while curr != cubes_[ int( starting_position[0]  ) ]  [ int( starting_position[1]) ]:
                    
                    py.draw.rect(gridSurface, (255, 0, 100), (curr.print_row_col()[0] * diff, curr.print_row_col()[1] * diff, diff, diff), 1)
                    
                        
                    curr = path[curr]
            button("Refresh", 500, 610, 200, 59, red, red_light, BFS_loop )
            
            screen.blit(gridSurface, (0, 0))               
            py.display.update()
                
                
                
                
                
                
        if once:
            once = False
            screen.blit(gridSurface, (0, 0))
            py.display.update()  
                 
        
         
        clock.tick(60)
    py.quit()
    quit()

#############################**************************###############################






############        ##########         ########       ######################################################
############ ####### #########  ############## ###############################################
############ ######## ########  ###############     #####################################
############ ######### #######     ################# #############################################
############ ######## ########  ############## ###### ###########################################
############         #########  ###############     ###############################################




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
            if node and not node.get_cell_condition():
                if ( not visited[node.value]):
                    stack.append(node)
                    parentMap[node] = s
            

    return parentMap, traversal




def dfs_loop():
    
    gridSurface = py.Surface((601, 600))
    state = True
    rows = 50
    cols = 50
    grid = Grid(rows, cols, gridSurface, 601, 600 )
    clicked = None
    run = True
    once = True
    complete_first_time = False
    end = False
    start = False
    find = False
    starting_position = None
    end_position = None
    make_wall = False
    del_wall = False
    diff = WINDOW_WIDTH // 100
    blocks = {}
    cubes_ = grid.get_cubes()
    
    
    while run:
        
        
        
        
        
            
        #drawing the grid
        grid.draw()
        screen.fill(white)
        
        
              
        button("Start position", 50, 610, 135, 50, red, red_light)
        
        button("End position", 190, 610, 130, 50, red, red_light)
        
        button("Main Menu", 1070, 610, 110, 50, red, red_light, intro)
        button("Add blocks", 800, 610, 110, 50, red, red_light)
        button("Remove blocks", 920, 610, 140, 50, red, red_light)
        for event in py.event.get():
            if event.type == py.QUIT:
                run = False
            if event.type == py.MOUSEBUTTONDOWN:
                pos = py.mouse.get_pos()
                clicked = grid.get_cord(pos)
        
        
        
        
                
        
        if state: #pause button imitator
            # if some one of the button is clicked then the it performs the action related to it
            
            if clicked:
                
                if (50 + 135) > pos[0] > 50 and (610 + 50) > pos[1] > 610:
                    start = True
                    
                if (190 + 130) > pos[0] > 190 and (610 + 50) > pos[1] > 610:
                    start = False
                    end = True
                if end_position and starting_position:
                    if not once:
                        if (500 + 200) > pos[0] > 500 and (610 + 50) > pos[1] > 610:
                            find = True
                            end = False
                if (800 + 110) > pos[0] > 800 and (610 + 50) > pos[1] > 610:
                    start = False
                    end = False
                    find = False
                    make_wall = True       
                if (920 + 140) > pos[0] > 920 and (610 + 50) > pos[1] > 610:
                    start = False
                    end = False
                    find = False
                    make_wall = False
                    del_wall = True 
            
            
            
            
            if start: # if start is clicked then we can then select some box in the grid and it will be highlighted in red color
                    if blocks: #showing the blocked boxes
                        for i in blocks.values():
                            py.draw.rect(gridSurface, (0, 0, 0), (i[0] * diff, i[1] * diff, diff, diff))
                        
                    grid.select_start(clicked[0], clicked[1])
                    starting_position = clicked
                    screen.blit(gridSurface, (0, 0))
                    py.display.update()   
                        
            elif end: # likewise for the end position but in pink color
                    if blocks: #showing the blocked boxes
                        for i in blocks.values():
                            py.draw.rect(gridSurface, (0, 0, 0), (i[0] * diff, i[1] * diff, diff, diff))
                        
                    grid.select_end(clicked[0], clicked[1]) 
                    end_position = clicked
                    if starting_position:
                        grid.select_start(starting_position[0], starting_position[1])
                    
                            
                    button("Find path", 500, 610, 200, 59, red, red_light)
                    screen.blit(gridSurface, (0, 0))
                    py.display.update()  
            elif find: # the path finding occurs in here
                if blocks: #showing the blocked boxes
                        for i in blocks.values():
                            py.draw.rect(gridSurface, (0, 0, 0), (i[0] * diff, i[1] * diff, diff, diff))
                        
                    
                if (starting_position[0] < 50 and starting_position[1] <  50) and (end_position[0] < 50 and end_position[1] < 50):  
                    
                    grid.select_start(starting_position[0], starting_position[1])
                    
                    
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
                    state = False # to stop the same function going through again---kind of!
                    
                    
                    if not complete_first_time:  
                        complete_first_time = True
                        
                        screen.blit(gridSurface, (0, 0))
                        py.display.update()
                else:
                    if (starting_position[0] > 50 or starting_position[1] >  50):
                        button("Please Select a Starting Position!", 602, 10, 400, 50, red, red)
                        screen.blit(gridSurface, (0, 0))
                        py.display.update()
                    elif (end_position[0] > 50 or end_position[1] >  50):
                        button("Please select an End Position!", 602, 0, 400, 50, red, red)
                        screen.blit(gridSurface, (0, 0))
                        py.display.update()
                    else:
                        button("Please select both Positions!", 602, 0, 400, 50, red, red)
                        screen.blit(gridSurface, (0, 0))
                        py.display.update()     
                        
            
            elif make_wall:
                if (clicked[0] < 50 and clicked[1] <  50):  #to ensure that the clicked has tuple that is on the grid
                    bo = py.draw.rect(gridSurface, (0, 0, 0), (clicked[0] * diff, clicked[1] * diff, diff, diff))
                    blocks[  cubes_[clicked[0]] [clicked[1]].value  ] = clicked
                    grid.add_blocks(clicked[0], clicked[1])
                    screen.blit(gridSurface, (0, 0))
                    py.display.update(bo)
        
            elif del_wall:
                if (clicked[0] < 50 and clicked[1] <  50):  #to ensure that the clicked has tuple that is on the grid            
                    if blocks:
                        try:
                            del blocks[  cubes_[clicked[0]] [clicked[1]].value  ]
                            grid.remove_blocks(clicked[0], clicked[1])
                            for i in blocks.values():
                                py.draw.rect(gridSurface, (0, 0, 0), (i[0] * diff, i[1] * diff, diff, diff))
                            if starting_position and end_position:
                                button("Find path", 500, 610, 200, 59, red, red_light)
                                grid.select_start(starting_position[0], starting_position[1])
                                grid.select_end(end_position[0], end_position[1])
                            screen.blit(gridSurface, (0, 0))
                            py.display.update()
                        except Exception:
                            pass
                    else:
                        pass
        
        else:# same function but it just shows the same path but it will show all the path at once 
            
            if blocks: #showing the blocked boxes
                for i in blocks.values():
                    py.draw.rect(gridSurface, (0, 0, 0), (i[0] * diff, i[1] * diff, diff, diff))
            
                   
            grid.select_start(starting_position[0], starting_position[1])
            
            curr = cubes_[ int( end_position[0] ) ]  [ int(end_position[1]) ]
            grid.select_end(curr.print_row_col()[0], curr.print_row_col()[1])
            curr = path[curr]
            diff = WINDOW_WIDTH // 100
            while curr != cubes_[ int( starting_position[0]  ) ]  [ int( starting_position[1]) ]:
                    
                    py.draw.rect(gridSurface, (255, 0, 100), (curr.print_row_col()[0] * diff, curr.print_row_col()[1] * diff, diff, diff), 1)
                    
                        
                    curr = path[curr]
            button("Refresh", 500, 610, 200, 59, red, red_light, dfs_loop )
            
            screen.blit(gridSurface, (0, 0))               
            py.display.update()
                
                
                
       
                
        if once:
            once = False
            screen.blit(gridSurface, (0, 0))
            py.display.update()  
                 
        
         
        clock.tick(120)
    py.quit()
    quit()
    
#####################*************************#######################



########### #################     #######        ######## ##########      #######
######### ## ############### ##### ########## ########## # ######### #### #######
#######      ################# ############## ######### ### ######## #### #######
##### ###### ################### ############ ########       #######     ########
### ######## ############## ##### ########### ####### ####### ###### #### #######
############################     ############ ###### ######### ##### ##### ###### 


###!!!Important note: The a_star path finding takes the first path it had in the queue if there are two paths with same fScore!!!




def d(current, neighbor):
    x1, y1 = current.print_row_col()
    x2, y2 = current.print_row_col()
    # return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    return abs(x2-x1) + abs(y2-y1)


def heuristic(node, e):
    x1, y1 = node.print_row_col()
    x2, y2 = e.print_row_col()
    # return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    return abs(x2-x1) + abs(y2-y1)



def a_star(s, e, rows, cols):
    openSet = PriorityQueue()
    
    openSet.put((heuristic(s, e), 0, s))
    parentMap = {}
    visited = [False for i in range(rows * cols)]
    gScore = { i: float('inf') for i in range(rows*cols)}
    gScore[s.value] = 0
    traversal = []
    fScore = { i: float('inf') for i in range(rows*cols)}
    fScore[s.value] = 0
    
    count = 2500
    while not openSet.empty():
        current = openSet.get()
        
        if current[2] == e:
            
            break
        
        for neighbor  in current[2].show_connections():
            if neighbor and not neighbor.get_cell_condition():
                tentative_gScore = gScore[current[2].value] + d(current[2], neighbor)
                traversal.append(neighbor)
                # print(tentative_gScore)
                if tentative_gScore < gScore[neighbor.value]:
                    
                    count -= 1
                    parentMap[neighbor] = current[2]
                    gScore[neighbor.value] = tentative_gScore
                    fScore[neighbor.value] = gScore[neighbor.value] + heuristic(neighbor, e)
                    # print(fScore[neighbor.value],  neighbor.print_row_col())
                    openSet.put((fScore[neighbor.value], count,  neighbor))
                        
                    
                    visited[neighbor.value] = True
    return parentMap, traversal




def a_star_loop():
    
    gridSurface = py.Surface((601, 600))
    state = True
    rows = 50
    cols = 50
    grid = Grid(rows, cols, gridSurface, 601, 600 )
    clicked = None
    run = True
    once = True
    complete_first_time = False
    end = False
    start = False
    find = False
    starting_position = None
    end_position = None
    cubes_ = grid.get_cubes()
    make_wall = False
    del_wall = False
    blocks = {}
    diff = WINDOW_WIDTH // 100
    
    
    
    while run:
        
        
        
        
        
            
        #drawing the grid
        grid.draw()
        screen.fill(white)
        
        
              
        button("Start position", 50, 610, 135, 50, red, red_light)
        
        button("End position", 190, 610, 130, 50, red, red_light)
        button("Main Menu", 1070, 610, 110, 50, red, red_light, intro)
        button("Add blocks", 800, 610, 110, 50, red, red_light)
        button("Remove blocks", 920, 610, 140, 50, red, red_light)
        
        
        for event in py.event.get():
            if event.type == py.QUIT:
                run = False
            if event.type == py.MOUSEBUTTONDOWN:
                pos = py.mouse.get_pos()
                clicked = grid.get_cord(pos)
        
        
        
        
                
        
        if state: #pause button imitator
            # if some one of the button is clicked then the it performs the action related to it
            
            if clicked:
                
                if (50 + 135) > pos[0] > 50 and (610 + 50) > pos[1] > 610:
                    start = True
                    
                if (190 + 130) > pos[0] > 190 and (610 + 50) > pos[1] > 610:
                    start = False
                    end = True
                if end_position and starting_position:
                    if not once:
                        if (500 + 200) > pos[0] > 500 and (610 + 50) > pos[1] > 610:
                            find = True
                            end = False
                if (800 + 110) > pos[0] > 800 and (610 + 50) > pos[1] > 610:
                    start = False
                    end = False
                    find = False
                    make_wall = True    
                if (920 + 140) > pos[0] > 920 and (610 + 50) > pos[1] > 610:
                    start = False
                    end = False
                    find = False
                    make_wall = False
                    del_wall = True 
                       
                               
                
            if start: # if start is clicked then we can then select some box in the grid and it will be highlighted in red color
                    if blocks: #showing the blocked boxes
                        for i in blocks.values():
                            py.draw.rect(gridSurface, (0, 0, 0), (i[0] * diff, i[1] * diff, diff, diff))
                    
                    grid.select_start(clicked[0], clicked[1])
                    starting_position = clicked
                    screen.blit(gridSurface, (0, 0))
                    py.display.update()   
                        
            elif end: # likewise for the end position but in pink color
                    if blocks: #showing the blocked boxes
                        for i in blocks.values():
                            py.draw.rect(gridSurface, (0, 0, 0), (i[0] * diff, i[1] * diff, diff, diff))
                    
                    
                    
                    grid.select_end(clicked[0], clicked[1]) 
                    end_position = clicked
                    if starting_position:
                        grid.select_start(starting_position[0], starting_position[1])
                    
                            
                    button("Find path", 500, 610, 200, 59, red, red_light)
                    screen.blit(gridSurface, (0, 0))
                    py.display.update()  
            elif find: # the path finding occurs in here
                if blocks: #showing the blocked boxes
                    for i in blocks.values():
                        py.draw.rect(gridSurface, (0, 0, 0), (i[0] * diff, i[1] * diff, diff, diff))
                            
                               
                if (starting_position[0] < 50 and starting_position[1] <  50) and (end_position[0] < 50 and end_position[1] < 50):  
                    grid.select_start(starting_position[0], starting_position[1])
                    
                    
                    # the function returns the dictionary of the path that it took to get the end position but is in reverse order and also the traversal path
                    path, traversal = a_star(  cubes_[ int( starting_position[0]  ) ]  [ int( starting_position[1] ) ]   , cubes_[ int( end_position[0] ) ]  [ int(end_position[1]) ], rows, cols)
                    for i in traversal: #shows the traversal
                        bo = py.draw.rect(screen, (255, 100, 100), (i.print_row_col()[0] * diff, i.print_row_col()[1] * diff, diff, diff), 1)
                        py.time.delay(5)
                        py.display.update(bo)
                    
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
                else:
                    if (starting_position[0] > 50 or starting_position[1] >  50):
                        button("Please Select a Starting Position!", 602, 10, 400, 50, red, red)
                        screen.blit(gridSurface, (0, 0))
                        py.display.update()
                    elif (end_position[0] > 50 or end_position[1] >  50):
                        button("Please select an End Position!", 602, 0, 400, 50, red, red)
                        screen.blit(gridSurface, (0, 0))
                        py.display.update()
                    else:
                        button("Please select both Positions!", 602, 0, 400, 50, red, red)
                        screen.blit(gridSurface, (0, 0))
                        py.display.update()
            elif make_wall:
                if (clicked[0] < 50 and clicked[1] <  50):  #to ensure that the clicked has tuple that is on the grid
                    bo = py.draw.rect(gridSurface, (0, 0, 0), (clicked[0] * diff, clicked[1] * diff, diff, diff))
                    blocks[  cubes_[clicked[0]] [clicked[1]].value  ] = clicked
                    grid.add_blocks(clicked[0], clicked[1])
                    screen.blit(gridSurface, (0, 0))
                    py.display.update(bo)            
            elif del_wall:
                if (clicked[0] < 50 and clicked[1] <  50):  #to ensure that the clicked has tuple that is on the grid            
                    if blocks:
                        try:
                            del blocks[  cubes_[clicked[0]] [clicked[1]].value  ]
                            grid.remove_blocks(clicked[0], clicked[1])
                            for i in blocks.values():
                                py.draw.rect(gridSurface, (0, 0, 0), (i[0] * diff, i[1] * diff, diff, diff))
                            if starting_position and end_position:
                                button("Find path", 500, 610, 200, 59, red, red_light)
                                grid.select_start(starting_position[0], starting_position[1])
                                grid.select_end(end_position[0], end_position[1])
                            screen.blit(gridSurface, (0, 0))
                            py.display.update()
                        except Exception:
                            pass
                        
                        
                                    
        
        else:# same function but it just shows the same path but it will show all the path at once 
            if blocks: #showing the blocked boxes
                        for i in blocks.values():
                            py.draw.rect(gridSurface, (0, 0, 0), (i[0] * diff, i[1] * diff, diff, diff))
                        
        
            grid.select_start(starting_position[0], starting_position[1])
            
            curr = cubes_[ int( end_position[0] ) ]  [ int(end_position[1]) ]
            grid.select_end(curr.print_row_col()[0], curr.print_row_col()[1])
            curr = path[curr]
            
            while curr != cubes_[ int( starting_position[0]  ) ]  [ int( starting_position[1]) ]:
                    
                    py.draw.rect(gridSurface, (255, 0, 100), (curr.print_row_col()[0] * diff, curr.print_row_col()[1] * diff, diff, diff), 1)
                    
                        
                    curr = path[curr]
                    
            
            button("Refresh", 500, 610, 200, 59, red, red_light, a_star_loop )
            
            screen.blit(gridSurface, (0, 0))               
            py.display.update()
                
                
                
                
                
                
        if once:
            once = False
            screen.blit(gridSurface, (0, 0))
            py.display.update()  
                 
        
         
        clock.tick(60)
    py.quit()
    quit()
    
#####################*************************#######################



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