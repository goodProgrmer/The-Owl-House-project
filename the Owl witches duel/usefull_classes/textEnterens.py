import pygame
import global_var
from usefull_classes.button import button

class textEnterens:
    """place where the user can type text
    :param keySors: pointer to the list in which the opened window put pressed keys pygame index. keySors[0] is which Entrence is clicked, and after that keys index
    :param rect_tuple: the rect in which the enterens will be. its in the following format- (x,y,width,hight)
    :param color: entrence color (if you use it as rect)
    :param text: start text in the entrence (before the user type enything)
    :param font: text font (by difult it pygame.font.SysFont("Arial Nova", 50))
    :param enter_type: it can be password (then all the text is as *) or text (then it will be normal text)
    :type keySors: list of int (in index>=1) or object (in index==0)
    :type rect_tuple: (int,int,int,int)
    :type color: (int,int,int)-RGB
    :type text: string
    :type font: pygame.font
    :type enter_type: string"""
    def __init__(self,rect_tuple,color,text="",font=None, enter_type="text"):
        self.enter_type= enter_type

        if font==None:
            font= pygame.font.SysFont("Arial Nova", 50)
        
        self.rect_tuple= rect_tuple
        self.color=color
        self.text=text
        self.font= font
        self.image=pygame.transform.scale(pygame.image.load("images/system image/entry.png"), (rect_tuple[2],rect_tuple[3]))
        self.t=0
        self.shown_text= ""
        
        self.mouse_pushed= False
        self.pushed_keys= []
        self.clicked= False

        self.BLINGING_PERIOD=40

        #input correctency check
        if not enter_type in ["text","password"]:
            raise Exception('the type must be "text" or "password"')
    def tick(self):
        """pass 1 frame to the enterens"""
        self.shown_text= self.text
        if self.enter_type=="password":
            self.shown_text= "*"* len(self.shown_text)
                
        pressed = pygame.key.get_pressed()
        if self.clicked:
            self.t+=1
            if (self.t//self.BLINGING_PERIOD)%2==0:
                self.shown_text+="|"

            #pushed keys check
            for key in tuple(range(97,123))+tuple(range(48,57))+(8,32):
                if pressed[key] and not key in self.pushed_keys:
                    self.pushed_keys.append(key)
            
            #unpushed keys
            for key in self.pushed_keys:
                if not pressed[key]:
                    self.pushed_keys.remove(key)
                    if 97<=key<=122:
                        if pressed[pygame.K_LSHIFT] or pressed[pygame.K_RSHIFT]:
                            self.text+=chr(key-32)
                        else:
                            self.text+=chr(key)
                    if 48<=key<=57:
                        self.text+=chr(key)
                    if key==8:
                        self.text= self.text[:-1]
                    if key==32:
                        self.text+= " "

        self.paint()
        self.clicked_check()
            
    def get_text(self):
        """"return the text in the entrence
        :return: the text in the entrence
        :rtype: string"""
        return self.text

    def clicked_check(self):
        if pygame.mouse.get_pressed()[0]:
            self.mouse_pushed=True
        elif self.mouse_pushed:
            self.mouse_pushed=False
            mp=pygame.mouse.get_pos()
            if self.rect_tuple[0]<mp[0]<self.rect_tuple[0]+self.rect_tuple[2] and self.rect_tuple[1]<mp[1]<self.rect_tuple[1]+self.rect_tuple[3]:
                self.clicked= True
            else:
                self.clicked= False
                self.pushed_keys= []

    def set_text(self, string):
        """set the text of the entrence to the given string
        :param string: the given string
        :type string: string"""
        self.text= string

    def paint(self):
        """paint the button"""
        #rect
        if self.image==None:
            pygame.draw.rect(global_var.screen, self.color, pygame.Rect(self.rect_tuple))
        
        #image
        if self.image!=None:
            global_var.screen.blit(self.image,(self.rect_tuple[0],self.rect_tuple[1]))
        #text
        text = self.font.render(self.shown_text, True, (186, 201, 0))
        textRect = text.get_rect()
        textRect.center=(self.rect_tuple[0]+self.rect_tuple[2]/2,self.rect_tuple[1]+self.rect_tuple[3]/2)
        global_var.screen.blit(text,textRect)

