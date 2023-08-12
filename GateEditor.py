import pygame
from pygame.locals import * #constants
import sys 

BLACKCOLOR = (200,200,200)
WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 700
FRAMES_PER_SECOND = 60

#cell size limits
MAX_CELL_SIZE = 64
MIN_CELL_SIZE = 16
NORMAL_CELL_SIZE = 32

#varible s
cellsize = NORMAL_CELL_SIZE
origin_shift = [0,0]


#pyagme game smothing

pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT) , pygame.RESIZABLE)
pygame.display.set_caption("BGV SIMULATOR")
pygame.image.load("gateRes/icon.png")
pygame.display.set_icon(pygame.image.load("gateRes/icon.png"))
clock = pygame.time.Clock()


import BSV as bsv
import singltions.quick_bar_ as menu


manager = bsv.gateManager()

# manager.addGate(bsv.GATEBOX())
# manager.addGate(bsv.GATEBOX())
# manager.addGate(bsv.GATEBOX(bsv.GATE_BOX , 2 , 1 , [0,1,1,0]))
# manager.addGate(bsv.GATEBOX(bsv.GATE_BOX , 1 , 1 , [1,0]))
# manager.addGate(bsv.GATEBOX(bsv.TERMINAL_OUT,1))
# manager.addGate(bsv.GATEBOX(bsv.TERMINAL_OUT,1))


# manager.setpos(1 , [10,10])
# manager.setpos(2 , [10,40])
# manager.setpos(3 , [200,10])
# manager.setpos(4 , [200,50])
# manager.setpos(5 , [400,10])




# manager.setlabel(1 , "INP")
# manager.setlabel(2,  "INP")
# manager.setlabel(3 , "XOR")
# manager.setlabel(4 , "NOT")
# manager.setlabel(5 , "OUT")
# manager.setlabel(6 , "OUT")



# manager.simulate()


guimanager = bsv.gateGuiManager(manager)
guimanager.loadWindow(window)


#fgrid maker
def gridMaker(center , cellSize , color , limits):
    lx  , ly = limits
    clx = cellSize
    cx , cy = center
    normalcolor = color 
    
    for i in range(int(lx/(clx))):
        if i == 0: color = (200,0,0)
        else : color = normalcolor

        pygame.draw.line(window , color , (cx + i * clx , 0 ) , (cx + i * clx , ly))
        pygame.draw.line(window , color , ((cx - i * clx ), 0 ) , ((cx - i * clx ) ,ly ))

        pygame.draw.line(window , color , (0, cy+ i * clx ) , (lx, cy+ i * clx ) )
        pygame.draw.line(window , color , (0, cy- i * clx ) , (lx, cy- i * clx ) )
                 


def apply_transform(posvec , trs):
    return [ sum([v1 * v2 for v1 , v2 in zip(posvec , vec)]) for vec in trs]


while True:
    #window setting 
    WINDOW_HEIGHT , WINDOW_WIDTH = window.get_height() , window.get_width()

    #clearing the screen 
    window.fill(BLACKCOLOR)

    gridMaker((WINDOW_WIDTH/2  + origin_shift[0] , WINDOW_HEIGHT/2 + origin_shift[1]) , cellsize , (100,100,100) , [WINDOW_WIDTH , WINDOW_HEIGHT])


    for event in pygame.event.get(): #event loop
        if event.type == pygame.QUIT: 
            pygame.quit() 
            sys.exit()

        #here we are scalling the cellesize
        if event.type == pygame.MOUSEWHEEL:
            if event.y < 0:
                cellsize = min(cellsize+1 , MAX_CELL_SIZE)
            else:
                cellsize = max(cellsize-1 , MIN_CELL_SIZE)
            
            guimanager.setScales(cellsize/NORMAL_CELL_SIZE)
            print(cellsize/NORMAL_CELL_SIZE)
        
        #here is the origin shift
        
        if pygame.key.get_pressed()[pygame.K_LSHIFT] and pygame.mouse.get_pressed()[0]:
            mx  , my = pygame.mouse.get_pos()
            origin_shift = [ mx - WINDOW_WIDTH/2 , my - WINDOW_HEIGHT/2]
            guimanager.setOrigins(origin_shift , globalOrigin = [WINDOW_WIDTH/2 , WINDOW_HEIGHT/2])
            pass

       
       
        guimanager.renderevent(event)

    
   
    


    guimanager.renderGates()





    pygame.display.update()
    clock.tick(FRAMES_PER_SECOND) 


