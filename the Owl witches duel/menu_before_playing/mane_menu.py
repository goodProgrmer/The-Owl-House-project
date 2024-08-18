import global_var
import pygame
from usefull_classes.button import button
import sentOperations.sendingOperations as sockF
from usefull_classes.elart import elart

def toOtherFile(file):
    """go to another window
    :param file: path to next window
    :type file: string"""
    global done
    global_var.nextRunFileName=file
    done=True

def logout():
    """this function called when the user decided to logout"""
    sockF.sendMesegTCP(global_var.server_TCP_sock,"LOGIN|LOGOUT")
    global_var.username= None
    toOtherFile("menu_before_playing.mane_menu")

def help():
    """called when the how to help you button pushed"""
    global_var.alert_data= ("you can watch our behind the scenes video on youtube\n(the owl house comp game behind the scenes) (please do it).\nthat how we get money",(500,0,600,150))

def main():
    """the code of this window. it's screen is in global_var.screen."""
    global done
    done = False
    clock = pygame.time.Clock()

    buttons=[button(lambda: toOtherFile("menu_before_playing.game_menu"),(700,175,200,100),(255,0,0),"game"),
             button(lambda: toOtherFile("menu_before_playing.login.login"),(1100,600,100,50),(255,0,0),"login",font= pygame.font.SysFont("Edwardian Script ITC", 40)),
             button(lambda: toOtherFile("settings.onePlayer"),(700,275,200,100),(255,0,0),"settings"),
             button(lambda: toOtherFile("menu_before_playing.about_us"),(700,375,200,100),(255,0,0),"about us"),
             button(help,(550,475,500,100),(255,0,0),"help you your free")]

    if global_var.username!=None:
        buttons[1].text= "logout"
        buttons[1].onclick= logout

    if not global_var.is_connected:
        global_var.unable(buttons[1])

    while not done:
            for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                            done = True
            global_var.for_menu_screen()

            for b in buttons:
                b.tick()

            global_var.before_menu_screen_display()

            if global_var.data=="unconnected exit":
                global_var.data= None
                if elart("you disconnected from the server",(600,10,300,100)):
                    done=True
            pygame.display.flip()
            clock.tick(24)
            

if __name__=="__main__":
        main()
else:
        print(__name__)
