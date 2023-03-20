import pygame
import random

from pause import pause

pygame.init()
pygame.font.init()

my_font = pygame.font.SysFont('Comic Sans MS', 30)
my_fontHeading = pygame.font.SysFont('Comic Sans MS', 50) 
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 155, 0)
bright_green = (0, 255, 0)
bright_red = (238, 75, 43)

display_width = 800
display_height = 600

display = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Menu')
 
game_over = False
play_result = ''
 
x1 = display_width/2
y1 = display_height/2

clock = pygame.time.Clock()

def play():
    pygame.display.set_caption("Snake")
    play = True
    block_size = 10
    FPS = 40
    
    x1 = 300
    y1 = 300

    randAppleX = round (random.randrange (0, display_width-30)/10.0)*10.0
    randAppleY = round (random.randrange (0, display_height-30)/10.0)*10.0

    x1_change = 0
    y1_change = 0
    while play:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -block_size
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = block_size
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -block_size
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = block_size
                    x1_change = 0
                elif event.key == pygame.K_a:
                    x1_change = -block_size
                    y1_change = 0
                elif event.key == pygame.K_d:
                    x1_change = block_size
                    y1_change = 0
                elif event.key == pygame.K_w:
                    y1_change = -block_size
                    x1_change = 0
                elif event.key == pygame.K_s:
                    y1_change = block_size
                    x1_change = 0
                elif event.key == pygame.K_q:
                    return 'quit game'
                elif event.key == pygame.K_p:
                    pause()
        if x1 >= display_width or x1 < 0 or y1 >= display_height or y1 < 0:
            return 'hit border'

        x1 += x1_change
        y1 += y1_change
        
        display.fill(white)
        pygame.draw.rect(display, red, [randAppleX, randAppleY, block_size, block_size])
        pygame.draw.rect(display, green, [x1, y1, block_size*2, block_size*2])

        if x1 == randAppleX and y1 == randAppleY:
            print('ate the apple')
            randAppleX = round (random.randrange (0, display_width-30)/10.0)*10.0
            randAppleY = round (random.randrange (0, display_height-30)/10.0)*10.0

        pygame.display.update()
        clock.tick(FPS)