import pygame 
pygame.init()


WHITE = (250,250,250)
BLACK = (0,0,0)
RED = (255,0,0)

FPS = 60

WIDTH, HEIGHT = 600,600
TEXT_WIDTH, TEXT_HEIGHT = 270,180
ARROW_WIDTH_1 = 240
ARROW_WIDTH_2 = 350
ARROW_HEIGTH = 240

window = pygame.display.set_mode((WIDTH,HEIGHT))

arrow_left_font = pygame.font.SysFont('impact',40)
arrow_right_font = pygame.font.SysFont('impact',40)

play_font= pygame.font.SysFont('impact',40)
quit_font = pygame.font.SysFont('impact',40)


def menu_draw_window():
    window.fill(BLACK)
  
    arrow_left_text = arrow_left_font.render('>',1,RED)
    arrow_right_text = arrow_right_font.render('<',1,RED)
    play_text = play_font.render('Play',1,WHITE)
    quit_text = quit_font.render('Quit',1,WHITE)
    window.blit(arrow_left_text,(ARROW_WIDTH_1,ARROW_HEIGTH))
    window.blit(arrow_right_text,(ARROW_WIDTH_2,ARROW_HEIGTH))
    window.blit(play_text,(TEXT_WIDTH,TEXT_HEIGHT+60))
    window.blit(quit_text,(TEXT_WIDTH,TEXT_HEIGHT+120))

    pygame.display.update()

def menu_arrow(keys_pressed):

    global ARROW_HEIGTH
    global ARROW_WIDTH_1
    global ARROW_WIDTH_2

    if keys_pressed[pygame.K_w] and ARROW_HEIGTH > 240:
        ARROW_HEIGTH -= 60
        pygame.time.wait(100) 
    
    if keys_pressed[pygame.K_s] and ARROW_HEIGTH < 300:
        ARROW_HEIGTH += 60
        pygame.time.wait(100) 

    if ARROW_HEIGTH == 180 or ARROW_HEIGTH == 360:
        ARROW_WIDTH_1 = 240
        ARROW_WIDTH_2 = 350


def menu_():
    
    run = True
    clock = pygame.time.Clock()

    while run:
        clock.tick(FPS)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
        keys_pressed = pygame.key.get_pressed()


        if keys_pressed[pygame.K_SPACE] and ARROW_HEIGTH == 240:
            run = False
        if keys_pressed[pygame.K_SPACE] and ARROW_HEIGTH == 300:
            run = False
            pygame.quit()
     


        
        menu_draw_window()
        menu_arrow(keys_pressed)
           

        
        

