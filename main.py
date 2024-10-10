from Misc.misc import clear
from States.menu_inicial import MenuInicial
from States.menu_play import MenuPlay

menu_inicial = MenuInicial()
menu_play = None

# não use a palavra scene


def start():
    run = True
    play = False

    while run:
        if play is False:
            hero = None
            try:
                hero, seed_value = menu_inicial.draw_menu()
                clear()
            except:
                clear()
                hero, seed_value = menu_inicial.draw_menu()
                clear()
            if hero:
                global menu_play
                menu_play = MenuPlay(hero, seed_value)
                play = True
        else:
            play = menu_play.draw_menu()
            clear()


if __name__ == '__main__':
    start()
