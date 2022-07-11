import pygame 
pygame.init()
import os

WHITE = (250,250,250)
BLACK = (0,0,0)
RED = (255,0,0)
GREEN = (127,255,0)
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

head_img = pygame.image.load(os.path.join('file_snake','white.png'))
head = pygame.transform.scale(head_img,(20,20))

def menu_draw_window(snake,tail_list):
    window.fill(BLACK)
    
    arrow_left_text = arrow_left_font.render('>',1,GREEN)
    arrow_right_text = arrow_right_font.render('<',1,GREEN)
    play_text = play_font.render('Play',1,WHITE)
    quit_text = quit_font.render('Quit',1,WHITE)
    a = 0
    while a < 1 and len(tail_list) > 1:
        a += 1
        tail = pygame.Rect(tail_list[len(tail_list)-a][0],tail_list[len(tail_list)-a][1],20,20)
        pygame.draw.rect(window,GREEN,tail)
    
    window.blit(arrow_left_text,(ARROW_WIDTH_1,ARROW_HEIGTH))
    window.blit(arrow_right_text,(ARROW_WIDTH_2,ARROW_HEIGTH))
    window.blit(play_text,(TEXT_WIDTH,TEXT_HEIGHT+60))
    window.blit(quit_text,(TEXT_WIDTH,TEXT_HEIGHT+120))
    window.blit(head,(snake.x,snake.y))
    pygame.display.update()

def menu_arrow(keys_pressed):
    global ARROW_HEIGTH
    if keys_pressed[pygame.K_w] and ARROW_HEIGTH > 240:
        ARROW_HEIGTH -= 60
        pygame.time.wait(60) 
    
    if keys_pressed[pygame.K_s] and ARROW_HEIGTH < 300:
        ARROW_HEIGTH += 60
        pygame.time.wait(60)

def tail_location_create(tail_list,snake):
    if snake.x % 20 == 0 and snake.y % 20 == 0:
        list_space = []
        list_space.append(snake.x)
        list_space.append(snake.y)
        tail_list.append(list_space)
    if len(tail_list) > 2:
        tail_list.remove(tail_list[0])

def snake_controll(snake,speed):
        snake.y += speed

def tp(snake):
    if snake.x > 599:
        snake.x = 0
    elif snake.x < -1:
        snake.x = 600
    if snake.y < -1:
        snake.y = 600
    elif snake.y > 599:
        snake.y = 0

def game_menu():
    
    run = True
    clock = pygame.time.Clock()
    snake = pygame.Rect(400,100,20,20)
    speed = 5
    tail_list = []

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
        tp(snake)
        tail_location_create(tail_list,snake)
        snake_controll(snake,speed)
        menu_arrow(keys_pressed)
        menu_draw_window(snake,tail_list)
