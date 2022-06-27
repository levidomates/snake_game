
import pygame
import os 
import random
pygame.init()

run = True
list1 = []
tail_location = []
FPS = 60
SPEED = 5
WIDTH, HEIGTH = 600,600
FOOD_x, FOOD_y = 200,200
BLACK = (0,0,0)
WHITE = (250,250,250)
RED = (255,64,64)
GREEN = (127,255,0)
FOOD_COUNT = 0
snake_x, snake_y = 200, 200
controller = 1
window = pygame.display.set_mode((WIDTH,HEIGTH))
pygame.display.set_caption('sneak game')
clock = pygame.time.Clock()
snake_img = pygame.image.load(os.path.join('file_snake','white.png'))
SNAKE = pygame.transform.scale(snake_img,(20,20))

wait = 0


flag1 = False
flag2 = False
flag3 = False
flag4 = True

flag5 = True
flag6 = True
flag7 = True
flag8 = True

def list_maker():
    x,y = 20,20
    while True:
        list2 = []
        list2.append(x)
        list2.append(y)
        list1.append(list2)
        x += 20
        if x == WIDTH -20:
            y += 20
            x = 20
        if y == HEIGTH -20:
            break
    
def chooser():
    global FOOD_x
    global FOOD_y
    global list1
    global FOOD_COUNT
    c = 0
    while c < 1:
        list2 = random.choice(list1)
        if list2 not in tail_location:
            FOOD_x = list2[0]
            FOOD_y = list2[1]
            c += 1
            FOOD_COUNT += 1

def tail_location_create(snake):
    global tail_location
    if snake.x % 20 == 0 and snake.y % 20 == 0:
        list_space = []
        list_space.append(snake.x)
        list_space.append(snake.y)
        tail_location.append(list_space)
    if len(tail_location) > FOOD_COUNT + 1:
        tail_location.remove(tail_location[0])

    
def draw_window(snake,FOOD):
    global FOOD_COUNT
    global tail_location
    window.fill(BLACK)
   
    a = 0
    while a < FOOD_COUNT:
        a += 1
        snake_tail = pygame.Rect(tail_location[len(tail_location)-a][0],tail_location[len(tail_location)-a][1],20,20)
        pygame.draw.rect(window,GREEN,snake_tail)
    
    pygame.draw.rect(window, RED, FOOD)
    window.blit(SNAKE,(snake.x,snake.y))
    pygame.display.update()

def key_controller(snake,keys_pressed):

    global flag1
    global flag2
    global flag3
    global flag4
    global tail_location
    
  
    if snake.x % 20 == 0 and snake.y % 20 == 0 and len(tail_location) > 0:
        if keys_pressed[pygame.K_w] and flag5 == True and tail_location[len(tail_location)-2][0] != tail_location[len(tail_location)-1][0]:
            flag1 = True
            flag2 = False
            flag3 = False
            flag4 = False

        if keys_pressed[pygame.K_s] and flag6 == True and tail_location[len(tail_location)-2][0] != tail_location[len(tail_location)-1][0]:
            flag1 = False
            flag2 = True
            flag3 = False
            flag4 = False
                
        if keys_pressed[pygame.K_a] and flag7 == True and tail_location[len(tail_location)-2][1] != tail_location[len(tail_location)-1][1]:
            
            flag1 = False
            flag2 = False
            flag3 = True
            flag4 = False

        if keys_pressed[pygame.K_d] and flag8 == True and tail_location[len(tail_location)-2][1] != tail_location[len(tail_location)-1][1]:
            flag1 = False
            flag2 = False
            flag3 = False
            flag4 = True

            
def progress(snake):

    global SPEED
    global flag1
    global flag2
    global flag3
    global flag4

    if flag1 == True:
        snake.y -= SPEED
    if flag2 == True:
        snake.y += SPEED
    if flag3 == True:
        snake.x -= SPEED
    if flag4 == True:
        snake.x += SPEED
          

def teleportation(snake):
    if snake.x == 580:
        snake.x = 20
    elif snake.x == 0:
        snake.x = 580
    elif snake.y == 580:
        snake.y = 20
    elif snake.y == 0:
        snake.y = 580  

def pause(keys_pressed):    
    if keys_pressed[pygame.K_ESCAPE]:
        while True:
            pygame.time.wait(1000)
            if keys_pressed[pygame.K_ESCAPE]:   
                break



def main(): 
    global tail_location
    global FOOD_COUNT
    global snake
    global FOOD_x
    global FOOD_y
    global flag1
    global flag2
    global flag3
    global flag4

    run = True
    list_maker()
    snake = pygame.Rect(100, 200, 20, 20)
    while run:
        
        clock.tick(FPS)
        FOOD = pygame.Rect(FOOD_x, FOOD_y, 20, 20)
       
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        if snake.x == FOOD_x and snake.y == FOOD_y:
            chooser()
            
        list_space = []
        list_space.extend(tail_location)
        if [snake.x,snake.y] in list_space:
            list_space.remove([snake.x,snake.y])
        if [snake.x,snake.y] in list_space and len(tail_location) > 3:
            tail_location = []
            FOOD_COUNT = 0
            snake.x,snake.y = 100,200
            FOOD_x, FOOD_y = 200,200
            flag1 = False
            flag2 = False
            flag3 = False
            flag4 = True
            run = False
        keys_pressed = pygame.key.get_pressed()
        
        key_controller(snake,keys_pressed)
        draw_window(snake,FOOD)
        progress(snake)
        teleportation(snake)
        tail_location_create(snake)
       
        
    



