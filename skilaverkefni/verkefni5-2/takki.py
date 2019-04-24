#Höfundur: Huginn Þór Jóhannsson
import pygame
pygame.font.init()
myfont=pygame.font.SysFont("monospace",15)
print_text=lambda x,color:myfont.render(x,False,color)
class Takki:
    def __init__(self,window,texti,posx,posy,action=None):
        self.texti=texti
        pygame.draw.rect(window,(255,0,0),pygame.Rect(posx,posy,180,60))
        window.blit(print_text("{}".format(texti),(255,255,255)),(posx,posy))
        def button():
            mouse=pygame.mouse.get_pos()
            click=pygame.mouse.get_pressed()
            if posx+180 > mouse[0] > posx and posy+60 > mouse[1] > posy:
                pygame.draw.rect(window,(255,255,255),(posx,posy,180,60))
                window.blit(print_text("{}".format(texti),(255,0,0)),(posx,posy))
                if click[0] == 1 and action!=None:
                    action()
        button()
