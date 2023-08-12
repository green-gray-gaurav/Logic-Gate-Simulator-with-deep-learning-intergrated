import pygame
import pygwidgets
import vectors

class TextMesh():
    def __init__(self  , text , x , y , bg , fg , size , font = "freesansbold.ttf") -> None:
        self.text = text
        self.x = x 
        self.y = y
        self.bg  = bg
        self.fg = fg
        self.size = size
        self.font = font
        self.window  = None
        self.TextRect = None
        self.visible = True

        #here we are doing this inital assignment

        font = pygame.font.Font(self.font , self.size)
        text = font.render(self.text , True , self.fg , self.bg  )
        rect = text.get_rect()
        self.TextRect = rect

        pass
    def loadWindow(self , window):
        self.window = window
        pass
    def renderWidget(self):
        if self.visible:
            font = pygame.font.Font(self.font , self.size)
            text = font.render(self.text , True , self.fg , self.bg  )
            rect = text.get_rect()
            self.TextRect = rect
            rect.center = (self.x + rect.width/2 , self.y + rect.height/2)
            self.window.blit(text , rect )
        pass

#a little modifies class

class TextMeshPro(TextMesh):
    def __init__(self, text, x, y, bg, fg, size, font="freesansbold.ttf" , rectdim = (10,10)) -> None:
        super().__init__(text, x, y, bg, fg, size, font)
        self.rectdim = rectdim
    
    def loadWindow(self, window):
        return super().loadWindow(window)
    
    def renderWidget(self):
        font = pygame.font.Font(self.font , self.size)
        text = font.render(self.text , True , self.fg , self.bg  )
        rect = text.get_rect()
        self.TextRect = rect
        rect.center = (self.x , self.y)
        rect.width , rect.height = self.rectdim
        self.window.blit(text , rect )
    



#here we have a button class inheritesfrom textmesh class

class Button(TextMesh):
    def __init__(self, text, x, y, bg, fg, size, trigger  , font="freesansbold.ttf" ) -> None:
        super().__init__(text, x, y, bg, fg, size, font)
        #here we have exta
        self.mouseevent = "out"
        self.triggerFunctions = [lambda : 0, lambda :0,lambda :0 ,lambda : 0]
        self.triggerFunction = trigger

        self.onenterbg = (255,255,255)
        self.onleavebg = (0,0,0)
        self.onenterfg = (255,0,0)
        self.onleavefg = (255,255,255)
        self.ontriggerbg = (255,255,255)
        self.ontriggerfg = (0,0,0)

        self.active = True

        


        #retention proopeties // deplicates
        #//
        self.retainBg = self.bg
        self.retainFg = self.fg


    def loadWindow(self, window):
        return super().loadWindow(window)
    
    def renderWidget(self):
        return super().renderWidget()
    
    def eventRender(self , event):
        
        if event == None or not self.active: 
            
            return

        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.TextRect.collidepoint(event.pos):
                self.triggerFunction()

                self.bg = self.ontriggerbg
                self.fg = self.ontriggerfg
                
                pass

        if event.type == pygame.MOUSEMOTION:
            if self.mouseevent == "out":
                if self.TextRect.collidepoint(event.pos):
                    #on mouse enter

                    self.triggerFunctions[0]()

                    #setitng the buttons proerties
                    self.bg = self.onenterbg
                    self.fg = self.onenterfg

                    self.mouseevent = "in"
                    pass

            if self.mouseevent == "in":
                if not self.TextRect.collidepoint(event.pos):
                    #on mouse leave
                    self.triggerFunctions[1]()

                    self.bg = self.onleavebg
                    self.fg = self.onleavefg

                    self.mouseevent = "out"
                    pass
            
            if self.mouseevent == "in" :

                if self.TextRect.collidepoint(event.pos):

                    self.triggerFunctions[2]()

                    
                    #mouse hover
                    self.mouseevent = "in"
                    pass

            if event.type == pygame.MOUSEMOTION:
                
                if self.mouseevent == "out" :
                    if not self.TextRect.collidepoint(event.pos):
                        #on mouse enter

                        

                    #setitng the buttons proerties
                        self.bg = self.retainBg
                        self.fg = self.retainFg

                        self.mouseevent = "out"
                        pass
            




                


        pass 

        
    
   

class textInput():
    def __init__(self, x , y , width , fontsize = 30 , textcolor = (0,0,0) , bg = (255,255,255) , placeholder = "" , triggger = lambda : 0) -> None:
        self.window = None
        self.x = x
        self.y = y
        self.width = width
        self.fontsize = fontsize
        self.textColor = textcolor
        self.bg = bg
        self.placeholder = placeholder
        self.InputField = None
        self.value = None
        self.trigger = triggger
        self.visible = True
        self.active = True
        pass

    def loadWindow(self , window):
        
        self.window = window
        self.InputField = pygwidgets.InputText(self.window , (self.x , self.y) , self.placeholder , None , self.fontsize , self.width , self.textColor , self.bg)
        
        pass
    def renderWidget(self):
        if self.visible:
            self.InputField.draw()

        pass
    def eventHandler(self , event):
        if self.active:
            if self.InputField.handleEvent(event):
                self.value = self.InputField.getValue()
                self.trigger()
        pass


class textureRect():
    def __init__(self ,x , y , width , height , color  = (200,200,200 ), borders = [-1,-1,-1,-1]) -> None:
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.borders = borders
        self.visible = True
        

        self.window = None

        self.innerRect = pygame.Rect(self.x , self.y , self.width , self.height)
        pass

    def loadWindow(self, window):
        self.window = window
        pass
       
    
    def renderWidget(self):
        if self.visible:
            self.innerRect = pygame.Rect(self.x , self.y , self.width , self.height)
            pygame.draw.rect(self.window , self.color , self.innerRect , border_top_left_radius= self.borders[0] , border_top_right_radius= self.borders[1] , border_bottom_left_radius= self.borders[2], border_bottom_right_radius= self.borders[3])
            
        pass


class Navbar():
    def __init__(self , x , y , rate = 1 , limits = 100 , width = 100 , outVisible = False) -> None:
        self.x =x
        self.y =y
        self.movY = y
        self.limits = limits
        self.width = width
        self.scollerRate = rate
        self.motion = 0
        self.rect = pygame.Rect(self.x , self.y , self.width  , self.limits)

        pass

    def renderEvent(self , event):
        #scolling the in sidethe boundry
       
        
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            if event.type == pygame.MOUSEWHEEL:
                if event.y > 0 :
                    self.motion += self.scollerRate
                    self.movY += self.scollerRate
                   
                else:
                    self.motion -= self.scollerRate
                    self.movY -= self.scollerRate
                 

    def renderTheWidgetByMotion(self, widget):
        #here we need tolimit this motion
        widget.y += self.motion

        pass

    def renderTheWidgetByPOs(self , widget):
        widget.y = self.movY
        pass

    def setDefaultPos(self):
        #making the things default
        self.movY = self.y

    def setDefaultMotion(self):
        self.motion = 0


    def outboundRenderHandle(self , widget ):
        if widget.y < self.y or widget.y > self.y + self.limits:
            #cant reder the widget
            pass
        else:
            #render the widget
            widget.renderWidget()
            pass




class interactiveShape():
    
    LAYER_ID = 0
    EVENT_COUNT = 0

    def __init__(self , x , y , shape , attrib = None , triggerFunc = None , toggle = False) -> None:
        self.x = x
        self.y = y
        self.shape = shape
        self.attrib = attrib
        self.triggerFunc = triggerFunc
        self.window = None
        self.toggle = toggle

        self.vectors = [[1,1 ,1]
                       ,[1,-1,1],
                        [-1,-1,1],
                        [-1,1,1]]
        self.transform = None

        self.colors = {'click':(200,0,0) , 'enter':(200,200,200) , 'leave' : (200,200,200) , 'normal':(200,200,0)}
        self.color  = self.colors['normal']
        #internal state
        self.triggerRect = None
        self.mouseevent = 'out'

        interactiveShape.LAYER_ID+=1
        

        pass
    def apply_transform(self, posvec , trs):
        return [ sum([v1 * v2 for v1 , v2 in zip(posvec , vec)]) for vec in trs]

    def setTransform(self, trans):
        self.transform = trans

    def loadWindow(self ,window):
        self.window = window
        self.renderWindow()
        pass

    def renderEvent(self ,event):

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            interactiveShape.EVENT_COUNT+=1

            
            
            
               

            if self.triggerRect.collidepoint(event.pos):
               self.triggerFunc()
               self.color = self.colors['click']
                
            

        if event.type == pygame.MOUSEMOTION:
            if self.mouseevent == "out":
                if self.triggerRect.collidepoint(event.pos):
                    #on mouse enter

                    #setitng the buttons proerties
                    self.color = self.colors['enter']
                    self.mouseevent = "in"
                    pass

            if self.mouseevent == "in":
                if not self.triggerRect.collidepoint(event.pos):
                    #on mouse leave
                  

                    
                    self.color = self.colors['leave']
                    self.mouseevent = "out"
                    pass
            
            if self.mouseevent == "in" :
                if self.triggerRect.collidepoint(event.pos):
                    
                    #mouse hover
                    
                    self.mouseevent = "in"
                    pass

            if event.type == pygame.MOUSEMOTION:
                
                if self.mouseevent == "out" :
                    if not self.triggerRect.collidepoint(event.pos):
                        #on mouse enter
                        self.color = self.colors['normal']

                    #setitng the buttons proerties

                        self.mouseevent = "out"
                        pass

        pass

    def renderWindow(self):
        if self.shape == "circle":
            self.triggerRect = pygame.draw.circle(self.window , self.color , (self.x , self.y) , self.attrib[0])
            pass
        if self.shape == "rect":
            self.triggerRect = pygame.draw.rect(self.window ,  self.color  , pygame.Rect(self.x , self.y , self.attrib[0] ,self.attrib[1]))
            pass

        if self.shape == "rectT":

            points = [self.apply_transform(vec , self.transform)[:-1] for vec in self.vectors]
            self.triggerRect = pygame.draw.polygon(self.window ,  self.color  , points)
            
            pass

        if self.shape == "rectU":
            self.triggerRect = pygame.draw.rect(self.window ,  self.color  , pygame.Rect(self.x , self.y , self.attrib[0] ,self.attrib[1]) , self.attrib[2])
            pass
        if self.shape == "triangle":
            points = self.__triangle((self.x , self.y) ,self.attrib[0] , self.attrib[1])
            self.triggerRect = pygame.draw.polygon(self.window ,  self.color  , points)
            pass
        if self.shape == "line":
            self.triggerRect = pygame.draw.line(self.window , self.color , (self.x , self.y), (self.attrib[0] , self.attrib[1]) , self.attrib[2])

        if self.shape == "poly":
            points = [vectors.vector2D(*v) + vectors.vector2D(self.x ,self.y) for v in self.attrib]
            points = [v.toArray() for v in points]
            self.triggerRect = pygame.draw.polygon(self.window ,  self.color  , points)


        #here can add mosre shape

        pass
    pass

    def __triangle(self , origin , direction , mag):
        originVec = vectors.vector2D().fromArray(origin)
        vec = vectors.vector2D().fromArray(direction).normalized()
        vec2 = vec.rotateBy(120)
        vec3 = vec2.rotateBy(120)

        polypoints = [(vec * mag) , vec2 * mag , vec3 * mag , vec * mag ]

        return [(v + originVec).toArray()  for v in polypoints]
        pass
    
    def setColor(self , to ,color , baseColor = None):
        self.colors[to] = color
        if baseColor:
            self.color = baseColor
        pass

    def getPos(self):
        return (self.x , self.y)
    






    


        
