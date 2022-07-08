import pygame
import os
import random

BLACK = (0,0,0)
WHITE = (250,250,250)
RED = (255,64,64)
GREEN = (127,255,0)

WIDTH, HEIGHT = 600,600

window = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('sneak game')

head_img = pygame.image.load(os.path.join('file_snake','white.png'))
head = pygame.transform.scale(head_img,(20,20))



flag1 = True
flag2 = False
flag3 = False
flag4 = False


def list_maker(list1):
    x,y = 40,40
    while True:
        list2 = []
        list2.append(x)
        list2.append(y)
        list1.append(list2)
        x += 20
        if x == WIDTH - 20:
            y += 20
            x = 40
        if y == HEIGHT - 20:
            break

def tail_location_create(tail_list,snake,FOOD_COUNT):
    if snake.x % 20 == 0 and snake.y % 20 == 0:
        list_space = []
        list_space.append(snake.x)
        list_space.append(snake.y)
        tail_list.append(list_space)
    if len(tail_list) > FOOD_COUNT + 1:
        tail_list.remove(tail_list[0])

def draw_window(FOOD_COUNT, FOOD, tail_list,snake):
    window.fill(BLACK)
    pygame.draw.rect(window,RED,FOOD)
    a = 0
    while a < FOOD_COUNT + 1:
        a += 1
        tail = pygame.Rect(tail_list[len(tail_list)-a][0],tail_list[len(tail_list)-a][1],20,20)
        pygame.draw.rect(window,GREEN,tail)
    window.blit(head,(snake.x,snake.y))
    pygame.display.update()


def snake_controll(snake,key_pressed,speed,snake_list):
    global flag1 
    global flag2
    global flag3 
    global flag4

    if snake.x % 20 == 0 and snake.y % 20 == 0:
        if key_pressed[pygame.K_w] and snake_list[0][0] != snake_list[1][0]:
            flag1 = True
            flag2 = False
            flag3 = False
            flag4 = False
        if key_pressed[pygame.K_s] and snake_list[0][0] != snake_list[1][0]:
            flag1 = False
            flag2 = True
            flag3 = False
            flag4 = False
        if key_pressed[pygame.K_a] and snake_list[0][1] != snake_list[1][1]:
            flag1 = False
            flag2 = False
            flag3 = True
            flag4 = False
        if key_pressed[pygame.K_d] and snake_list[0][1] != snake_list[1][1]:
            flag1 = False
            flag2 = False
            flag3 = False
            flag4 = True

    if flag1 == True:
        snake.y -= speed
    if flag2 == True:
        snake.y += speed
    if flag3 == True:
        snake.x -= speed
    if flag4 == True:
        snake.x += speed

def tp(snake):

    if snake.x > 599:
        snake.x = 0
    elif snake.x < -1:
        snake.x = 600
    if snake.y < -1:
        snake.y = 600
    elif snake.y > 599:
        snake.y = 0

def snake_cordinate(snake,snake_list):
    free_list = []
    free_list.append(snake.x)
    free_list.append(snake.y)
    snake_list.insert(0,free_list)

def SnakeGame():

    list1 = []
    tail_list = []
    food_list = [220,120]
    snake_list = []
    FPS = 60
    FOOD_COUNT = 0
    speed = 5
    snake = pygame.Rect(100,100,20,20)
    clock = pygame.time.Clock()
    list_maker(list1)
    run = True
    
    while run:
        clock.tick(FPS)
        FOOD = pygame.Rect(food_list[0],food_list[1],20,20)
        
        if snake.x == food_list[0] and snake.y == food_list[1]:
            FOOD_COUNT += 1
        if snake.x == food_list[0] and snake.y == food_list[1]:
            while True:
                food_list = []
                food_list = random.choice(list1)
                if food_list not in tail_list:
                    break

        list_space = []
        for i in range(0,len(tail_list)-1):
            list_space.append(tail_list[i])    
        if [snake.x,snake.y] in list_space:
            run = False
        if len(snake_list) > 2:
            snake_list.remove(snake_list[len(snake_list)-1])
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

        key_pressed = pygame.key.get_pressed()

        tp(snake)    
        tail_location_create(tail_list,snake,FOOD_COUNT)
        snake_controll(snake,key_pressed,speed,snake_list)
        snake_cordinate(snake,snake_list)
        draw_window(FOOD_COUNT,FOOD,tail_list,snake)
    
