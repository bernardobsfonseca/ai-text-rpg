from Misc.misc import clear
from States.menu_inicial import MenuInicial
from States.menu_play import MenuPlay

menu_inicial = MenuInicial()


def start():
    hero = None
    seed_value = None
    run = True
    play = False

    while run:
        if play is False:
            hero, seed_value = menu_inicial.draw_menu()
            clear()
            if hero:
                play = True
        else:
            menu_play = MenuPlay(hero, seed_value)
            play = menu_play.draw_menu()


if __name__ == '__main__':
    start()
