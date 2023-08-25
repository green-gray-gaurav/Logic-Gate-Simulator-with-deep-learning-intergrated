import pygame
import threading
from gui import LoadingGui
# from gesture_recognizer import JustureReq

# #gesture control
# gesture = JustureReq(True)
# handle = threading.Thread(target=gesture.main)
# handle.start()

pygame.init()
window = pygame.display.set_mode((800, 400) , pygame.RESIZABLE)
clock = pygame.time.Clock()

# shiftEvent = pygame.event.Event(768 , {'unicode': '', 'key': 1073742053, 'mod': 4098, 'scancode': 229, 'window': None})

# ctrlEvent = pygame.event.Event(769 , {'unicode': '', 'key': 1073742052, 'mod': 4096, 'scancode': 228, 'window': None})

lg = LoadingGui(100,100)
lg.loadWindow(window)
lg.startLoading()
a = pygame.event.get()
while True:
    
    # pygame.event.post(shiftEvent)
   
    for event in pygame.event.get():
        print(event , pygame.key.get_pressed()[pygame.K_LCTRL])
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_RSHIFT:
            print("Shift presesd")
            lg.againStartLoading()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_RCTRL:
            print("control presesd")
        if event.type == pygame.KEYDOWN and event.key == pygame.K_RALT:
            print("alt presesd")  
            lg.stopLoading()
    window.fill((200,200,200))

    lg.renderWidget()
    pygame.display.update()
    clock.tick(30) 
