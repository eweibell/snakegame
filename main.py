import pygame
 
from play import play
from showmenu import showmenu
from gameover import gameover

from default import game_over, play_result

pygame.display.set_caption('Menu')

while not game_over:
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    pygame.quit()
                    quit()
                if event.key == pygame.K_p:
                    play_result = play()
if play_result == 'hit border':
    print('calling game over')
    gameover('You hit the border')
else:
    print('calling showmenu')
    showmenu()

pygame.quit()
quit()