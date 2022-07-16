import pygame
pygame.init()

FPS = 60

BLACK = (0,0,0)
WHITE = (250,250,250)
RED = (255,64,64)
GREEN = (127,255,0)

WIDTH, HEIGHT = 600,600

clock = pygame.time.Clock()

window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('sneak_game')

play_font = pygame.font.SysFont('impact',50)
quit_font = pygame.font.SysFont('impact',50)

play_text = play_font.render('Play',1,WHITE)
quit_text = quit_font.render('Quit',1,WHITE)

arrow_font = pygame.font.SysFont('impact',40)
arrow_text = arrow_font.render('>',1,GREEN)

class Arrow_move():
    def __init__(self, height = 205):
        self.height = height
    def arrow_move(self,keys_pressed):
        if keys_pressed[pygame.K_w]:
            self.height = 205
        if keys_pressed[pygame.K_s]:
            self.height = 290
        window.blit(arrow_text,(110,self.height))

def draw_menu(arrow,keys_pressed):
    window.fill(BLACK)
    arrow.arrow_move(keys_pressed)
    window.blit(play_text,(150,200))
    window.blit(quit_text,(150,280))
    pygame.display.update()

def snake_menu():
    arrow = Arrow_move()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[pygame.K_SPACE] and arrow.height == 205:
            run = False
        if keys_pressed[pygame.K_SPACE] and arrow.height == 290:
            run = False
            pygame.quit()
        draw_menu(arrow,keys_pressed)

