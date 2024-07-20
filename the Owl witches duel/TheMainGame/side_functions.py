import pygame
import global_var
from usefull_classes.button import button


def count(font=None):
    """this stop the previoas window (without exit from it) and  start count of the start of the game.
    :return: true if the x button of the window was clicked, otherwise it returns false
    :rtype: bool"""
    global done

    if font==None:
        font = pygame.font.SysFont("Arial", 100)

    #screen preperation
    s= pygame.Surface((10000,10000))
    s.set_alpha(128)
    s.fill((0,0,0))
    global_var.screen.blit(s,(0,0))
    back_ground= global_var.screen.copy()

    #pygame variable init
    done= False
    clock = pygame.time.Clock()
    t=0

    #constents
    SECOND_T= 30 #the emount of frames that pass for 1 number

    NUMBERS= []

    for i in range(3):
        #NUMBERS.append(pygame.transform.scale(pygame.image.load("images/system image/count/X.png"), (400,100)))
        NUMBERS.append(pygame.image.load("images/system image/count/"+str(i+1)+".png"))

    while not done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
                    return True

            #print(t)
            global_var.screen.blit(back_ground,(0,0))

            #sending prpose paint
            img= NUMBERS[2-t//SECOND_T]
            rect= img.get_rect()
            rect.center= (800,400)
            global_var.screen.blit(img, rect)
            t+=1

            if 3-t//SECOND_T<=0:
                done=True
            
            pygame.display.flip()
            clock.tick(24)
    return False

def loading_display(end):
    #NOTE: end param is list with len=1 when end[0] is boolean (when end[0] is True the function stop its running)
    circle= pygame.image.load("TheMainGame/images/loading.png")
    surface= pygame.Surface((circle.get_width()*2,circle.get_width()*2)).convert_alpha()
    surface.fill((0,0,0,0))
    surface.blit(circle,(0,0))
    circle= surface
    print(type(surface),type(circle))
    angle= 0
    font = pygame.font.SysFont("Algerian", 50)
    text = font.render("loading", True, (186, 201, 0))
    clock = pygame.time.Clock()
    while not end[0]:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return True
        global_var.for_menu_screen()
        global_var.screen.blit(text,(550,300))
        to_draw= pygame.transform.rotate(circle,angle)
        rect= to_draw.get_rect()
        rect.center= (950,325)
        global_var.screen.blit(to_draw,rect)
        angle+= 3
        if angle%90==0:
            pass
            #print(angle)
        global_var.before_menu_screen_display()
        pygame.display.flip()
        clock.tick(30)
    return False
