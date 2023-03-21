import pygame

from play import play
from showmenu import showmenu
from default import game_over, my_font, my_fontHeading, white, black, red, green, bright_green, bright_red, display_width, display_height, display, x1, y1, clock, game_result

pygame.init()
pygame.font.init()
pygame.display.set_caption('Menu')

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
