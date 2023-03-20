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
pygame.display.set_caption('Menu')
 
game_over = False
play_result = ''
 
x1 = display_width/2
y1 = display_height/2

clock = pygame.time.Clock()

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