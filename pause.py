import pygame
from default import my_font, my_fontHeading, white, black, red, green, bright_green, bright_red, display_width, display_height, display, game_over, play_result, x1, y1, clock

pygame.init()
pygame.font.init()
pygame.display.set_caption('Menu')

def pause():
        paused = True
        display.fill(white)
        pygame.display.set_caption("Paused")
        pausedtext = my_fontHeading.render("Paused", True, bright_green)
        display.blit(pausedtext, (340,150))
        
        pausedtext2 = my_font.render("Press C to continue or Q to quit", True, black)
        display.blit(pausedtext2, (220,230))
        
        pygame.display.update()
        clock.tick(5)

        while paused:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_c:
                        paused = False
                    elif event.key == pygame.K_q:
                        pygame.quit()
                        quit()
