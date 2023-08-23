import pygame
from pygame.locals import * #constants
import sys 
from singltions.file_sl import basicSaving , saverLoader
from gui import InputFieldPro , LabelList , ImageButton
from shells.shells_base import shell
import webbrowser
from util_functions import Timer

#web
COMMUNITY_LINK ="https://sample-app-71dda.web.app"


BLACKCOLOR = (150,150,150)
WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 700
FRAMES_PER_SECOND = 70

#cell size limits
MAX_CELL_SIZE = 64
MIN_CELL_SIZE = 16
NORMAL_CELL_SIZE = 32

#varible s
cellsize = NORMAL_CELL_SIZE
origin_shift = [0,0]

#some call backs and small fucntipns 

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


#mamager obj saver
sl = saverLoader(WINDOW_WIDTH -  100 , 0  , 200,400)
sl.loadWindow(window)
sl.refeshButtons()

#gui mamnager
guimanager = bsv.gateGuiManager(manager)
guimanager.loadWindow(window)
sl.loadOnBoard(manager)

#communitybutton

com_but = ImageButton("gateRes/feedback_icon.png" , 16 , WINDOW_HEIGHT-64 , 32 , lambda : webbrowser.open_new_tab(COMMUNITY_LINK))
com_but.loadWindow(window)

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


#heres is teh shell
shl = shell(0 ,WINDOW_HEIGHT/3.7 , (200,50) , (200,300))
shl.loadWindow(window)
shl_but = ImageButton("gateRes/shell_icon.png" , 16 , WINDOW_HEIGHT-128  , 32 , shl.toggleActivity)
shl_but.loadWindow(window)

#get the obj refernce to shell
shl.setRefObj('manager' , manager)
shl.setRefObj('gui' , guimanager)



while True:
    

    #saving the stsus of the mamger object
    sl.saveIntoFile(manager)
    
    #window setting 

    #clearing the screen 
    window.fill(BLACKCOLOR)

    gridMaker((WINDOW_WIDTH/2  + origin_shift[0] , WINDOW_HEIGHT/2 + origin_shift[1]) , cellsize , (100,100,100) , [WINDOW_WIDTH , WINDOW_HEIGHT])


    for event in pygame.event.get(): #event loop
        if event.type == pygame.QUIT: 
            # bs.saveObj("saved/test.pkl" , manager)
            
            pygame.quit() 
            sys.exit()
        
        if pygame.key.get_pressed()[pygame.K_r]:
            guimanager = bsv.gateGuiManager(manager)
            guimanager.loadWindow(window)

        if event.type == pygame.VIDEORESIZE:
            WINDOW_HEIGHT , WINDOW_WIDTH = window.get_height() , window.get_width()

            sl.setAttributes(x = WINDOW_WIDTH - 100 )
            sl.refeshButtons()

            shl_but.setPos((16 , WINDOW_HEIGHT-128 ))
            com_but.setPos(( 16 , WINDOW_HEIGHT-64))
            pass

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
        sl.renderEvent(event)
        com_but.eventRender(event)
        
        shl.eventRender(event)
        shl_but.eventRender(event)
       
        
    shl.renderWindow()
    shl_but.renderWidget()
    guimanager.renderGates()
    sl.renderWindow()
    com_but.renderWidget()
   

    pygame.display.update()
    clock.tick(FRAMES_PER_SECOND) 

    


