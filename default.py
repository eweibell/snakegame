import pygame

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
 
game_over = False
play_result = ''
 
x1 = display_width/2
y1 = display_height/2

clock = pygame.time.Clock()