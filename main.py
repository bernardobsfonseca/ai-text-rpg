from Misc.misc import clear
from States.menu_inicial import MenuInicial
from States.menu_play import MenuPlay

menu_inicial = MenuInicial()
menu_play = None  # Inicializa menu_play como None


def start():
    run = True
    play = False

    while run:
        if play is False:
            hero, seed_value = menu_inicial.draw_menu()
            clear()
            if hero:
                # Apenas inicializa menu_play se houver um novo herói
                global menu_play  # Declarando como global para poder modificar a variável global dentro da função
                menu_play = MenuPlay(hero, seed_value)
                play = True
        else:
            play = menu_play.draw_menu()
            clear()


if __name__ == '__main__':
    start()
