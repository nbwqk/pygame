import pygame

pygame.init()
screen=pygame.display.set_mode([600,600])
keep_going=True

#pic=pygame.image.load("face.jpg")
#colorkey=pic.get_at((0,0))
#pic.set_colorkey(colorkey)
picx=0
picy=0
BLACK=(0,0,0)
#timer=pygame.time.Clock()

GREEN=(0,255,0)
radius=50

while keep_going:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            keep_going=False
        picx+=1
        picy+=1

        screen.fill(BLACK)
        #screen.blit(pic,(picx,picy))
        pygame.draw.circle(screen,GREEN,(picx,picy),radius)
        pygame.display.update()
        #timer.tick(60)

pygame.quit()