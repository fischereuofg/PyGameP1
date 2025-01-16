import pygame

pygame.init()

SCREEN_SIZE=(800,600)


screen = pygame.display.set_mode(SCREEN_SIZE)

run=True
clock = pygame.time.Clock() 

player = pygame.Rect((300,250,30,30))
wall = pygame.Rect((300000000000000000,250,30,30))
mapFile = open(r"map.txt","r")

mapX=int(mapFile.readline())
mapY=int(mapFile.readline())
print("%d %d" %(mapY,mapX))

mapArray=[]
for y in range(mapY):
    temp=mapFile.readline()
    
    mapArray.append(temp.split(' '))
    
for x in range(mapX): 
    print()
    for y in range(mapY):
        print(mapArray[x][y]+" ",end="")

while run:
    screen.fill((255,255,255))

    clock.tick(60) 
    for x in range(mapX): 
    
        for y in range(mapY):
            pygame.draw.rect(screen,(255,0,0),wall)
            
    pygame.draw.rect(screen,(255,0,0),player)

    key = pygame.key.get_pressed()

    if key[pygame.K_w]==True:
        player.move_ip(0,-1)
    if key[pygame.K_s]==True:
        player.move_ip(0,1)
    if key[pygame.K_d]==True:
        player.move_ip(1,0)
    if key[pygame.K_a]==True:
        player.move_ip(-1,0)    

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False
    
    pygame.display.update()
pygame.quit()

