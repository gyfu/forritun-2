#Höfundur: Huginn Þór Jóhannsson
from main import *
pygame.init()
pygame.font.init()
window=pygame.display.set_mode((800,640))
pygame.display.set_caption("Teningar")
myfont=pygame.font.SysFont("monospace",15)
window.fill((0,150,0))
running=True
clock=pygame.time.Clock()
clock_ticks=20
print_text=lambda x:myfont.render(x,False,(BLACK))
def mkdice(values):
    startpos=200
    ypos=100
    for x in values:
        pygame.draw.rect(window,(RED),pygame.Rect(startpos,ypos,60,60))
        window.blit(print_text("{}".format(x)),(startpos,ypos))
        startpos+=70
while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
        if event.type==pygame.KEYDOWN and event.key==pygame.K_ESCAPE:
            running=False
    mkdice(th_init)
    #Kasta aftur takki
    pygame.draw.rect(window,(RED),pygame.Rect(300,300,150,60))
    window.blit(print_text("Kasta aftur?"),(307,320))
    #Stig núna
    pygame.draw.rect(window,(RED),pygame.Rect(300,370,150,60))
    window.blit(print_text("Stig núna {}"),(307,390))
    #Heildarstig
    pygame.draw.rect(window,(RED),pygame.Rect(300,440,150,60))
    window.blit(print_text("Heildarstig: {}"),(307,460))


    pygame.display.update()
    clock.tick(clock_ticks)

pygame.quit()
#print(counter(),th_init,score(counter()))
