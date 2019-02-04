import pygame
 
FPS = 30
WIN_WIDTH = 500
WIN_HEIGHT = 100
rect_width = 50
rect_height = 50

WHITE = (255, 255, 255)
ORANGE = (255, 150, 100)
LIGHT_BLUE = (64, 128, 255) 
pygame.init()
 
clock = pygame.time.Clock()
 
screen = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
 
#  x та y - координати лівої верхньої межі
x = 0   
y = (WIN_HEIGHT - rect_height) / 2  

run = True
move = 0
while run:
    screen.fill(WHITE) 
    pygame.draw.rect(screen, (255,0,0), [x, y, rect_width, rect_height])
    pygame.display.update()

    x += move
    if x <= 0 :
        move = 5
    elif x >= WIN_WIDTH - rect_width:
        move -= 5
    
    
    
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            exit()
 
    clock.tick(FPS)