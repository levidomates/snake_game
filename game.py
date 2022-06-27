import menu
import snake_game

a = 0
while True:
    if a > -1:
        menu.menu_()
        a +=1
    if a > 0:
        snake_game.main()
        a -= 1
        