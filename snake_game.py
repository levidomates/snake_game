import pygame
import os 
import random
import menu

FPS = 60

BLACK = (0,0,0)
WHITE = (250,250,250)
RED = (255,64,64)
GREEN = (127,255,0)

WIDTH, HEIGHT = 600,620

clock = pygame.time.Clock()

window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('sneak_game')

head_img = pygame.image.load(os.path.join('file_snake','white.png'))
head = pygame.transform.scale(head_img,(20,20))

snake_head = pygame.Rect(100,100,20,20)
food = pygame.Rect(100,200,20,20)

class Snake():

    def __init__(self,speed,flag,snake_head):
        self.speed = speed
        self.flag = flag
        self.snake_head = snake_head

    def move(self,keys_pressed):
        if snake_head.x % 20 == 0 and snake_head.y % 20 == 0:
            if keys_pressed[pygame.K_w] and self.flag != 1:
                self.flag = 0
            if keys_pressed[pygame.K_s] and self.flag != 0:
                self.flag = 1
            if keys_pressed[pygame.K_d] and self.flag != 3:
                self.flag = 2
            if keys_pressed[pygame.K_a] and self.flag != 2:
                self.flag = 3
    
        if self.flag == 0:
            self.snake_head.y -= self.speed
        if self.flag == 1:
            self.snake_head.y += self.speed
        if self.flag == 2:
            self.snake_head.x += self.speed
        if self.flag == 3:
            self.snake_head.x -= self.speed

        if self.snake_head.x > 580:
            self.snake_head.x = 20
        elif self.snake_head.x < 20:
            self.snake_head.x = 580
        if self.snake_head.y > 580:
            self.snake_head.y = 20
        elif self.snake_head.y < 20:
            self.snake_head.y = 580

class Food():

    def __init__(self, food, food_list = []):
        self.food = food 
        self.food_list = food_list

    def list_maker(self,):
        x,y = 40,40
        while True:
            list2 = []
            list2.append(x) ,list2.append(y) 
            self.food_list.append(list2)
            x += 20
            if x == WIDTH - 20:
                y += 20
                x = 40
            if y == HEIGHT - 20:
                break

    def food_create(self,):
        list_space = random.choice(self.food_list)
        self.food.x,self.food.y = list_space[0],list_space[1]

class Tail():
    def __init__(self,tail_list=[]):
        self.tail_list = tail_list
    def tail_list_maker(self,FOOD_COUNT):
        if snake_head.x % 20 == 0 and snake_head.y % 20 == 0:
            list_space = []
            list_space.append(snake_head.x)
            list_space.append(snake_head.y)
            self.tail_list.append(list_space)
        if len(self.tail_list) > FOOD_COUNT + 1:
            self.tail_list.remove(self.tail_list[0])
    def tail_location_create(self,FOOD_COUNT):
        a = 0
        while a < FOOD_COUNT + 1 and len(self.tail_list) > 0:
            a += 1
            tail_img = pygame.Rect(self.tail_list[len(self.tail_list)-a][0],self.tail_list[len(self.tail_list)-a][1],20,20)
            pygame.draw.rect(window,GREEN,tail_img)

def draw_window(snake,prey,tail,FOOD_COUNT):
    window.fill(BLACK)
    pygame.draw.rect(window,RED,prey.food)
    tail.tail_location_create(FOOD_COUNT)
    window.blit(head,(snake.snake_head.x,snake.snake_head.y))
    pygame.display.update()

def main():
    snake = Snake(5,2,snake_head)
    prey = Food(food)
    tail = Tail()
    prey.list_maker()
    FOOD_COUNT = 1
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
        keys_pressed = pygame.key.get_pressed()
        if snake_head.x == food.x and snake_head.y == food.y:
            FOOD_COUNT += 1
            prey.food_create()
        if [snake_head.x,snake_head.y] in tail.tail_list:
            FOOD_COUNT = 1
            run = False
        tail.tail_list_maker(FOOD_COUNT)
        draw_window(snake,prey,tail,FOOD_COUNT)
        snake.move(keys_pressed)

while True:
    menu.snake_menu()
    main()
