import pygame

from play import play

from default import my_font, my_fontHeading, white, black, bright_green, display_height, display_width, display, clock

pygame.init()
pygame.font.init()

display = pygame.display.set_mode((display_width, display_height))

def showmenu():
    print('showmenu run')
    
    display.fill(white)
    startscreentext = my_fontHeading.render("Welcome to Snake ", True, bright_green)
    display.blit(startscreentext, (230,150))

    startscreentext2 = my_font.render("If you run into yourself, or the edges, you will die!", True, black)
    display.blit(startscreentext2, (80,230))

    startscreentext3 = my_font.render("The objective of the game is to eat red apples", True, black)
    display.blit(startscreentext3, (100,260))

    startscreentext4 = my_font.render("The more apples you eat, the longer you get", True, black)
    display.blit(startscreentext4, (120,290))

    startscreentext5 = my_font.render("Press P to play or pause, and Q to quit", True, black)
    display.blit(startscreentext5, (180,330))

    pygame.display.update()
    clock.tick(20)
        