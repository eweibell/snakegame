import pygame

from play import play
from showmenu import showmenu

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

def gameover(reason):
    print('game over')
    game_over = True
    while game_over:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        pygame.quit()
                        quit()
                    elif event.key == pygame.K_r:
                        game_over = False
                        play()
                    elif event.key == pygame.K_m:
                         game_over = False
                         showmenu()
        gameovertext = my_fontHeading.render("Game Over!", True, red)
        display.blit(gameovertext, (250, 150))
        gameovertext2 = my_font.render(reason, True, black)
        display.blit(gameovertext2, (245, 230))
        gameovertext3 = my_font.render("Press R to restart or Q to quit", True, black)
        display.blit(gameovertext3, (165, 260))

        pygame.display.update()
        clock.tick(20)