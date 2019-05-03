#Höfundur: Huginn Þór Jóhannsson
from Classes import *
#Glugga init
pygame.init()
win=pygame.display.set_mode((640,480))
pygame.display.set_caption("Space Invaders!")
#Entity init
player=Player(win,5,410)
def spawn_invaders():
    listi=[]
    x=5
    for n in range(9):
        listi.append(Invader(win,x,5))
        x+=69
    return listi
invaders=spawn_invaders()
#Main loop
running=True
while running:
    pygame.time.delay(100)
    for event in pygame.event.get():
        if event.type==pygame.QUIT or event.type==pygame.KEYDOWN and event.key==pygame.K_ESCAPE:
            running=False
    player.draw()
    for n in invaders:
        n.draw()
        #n.move()
        for missile in player.missiles:
            n.shot(missile.x,missile.y)
        if n.alive!=0:
            print("Dies")
    player.move()
    player.shoot()
    for n in player.missiles:
        n.draw()
        n.move()
        print(n.x,n.y)
    pygame.display.update()
    win.fill((0,0,0))
pygame.quit()


