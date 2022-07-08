import menu
import snake_game
flag1 = True
while True:
    if flag1 == True:
        menu.game_menu()
        flag1 = False
    if flag1 == False:
        snake_game.SnakeGame()
        flag1 = True
        