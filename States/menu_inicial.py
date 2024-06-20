from random import randint
from Characters.hero import Hero
from Misc import misc
from States.menu_base import MenuBase
from Ai.SceneAmbient import scene_ambient as sa
from Ai.SceneEnemy import scene_enemy as se


class MenuInicial(MenuBase):
    def __init__(self):
        super().__init__()

        print("Carregando...\n")

        sa.initialize_scene_embient()
        se.initialize_scene_enemy()

        misc.clear()

    def draw_menu(self):
        misc.draw_logo()
        misc.draw_line()
        print("1 - Novo Jogo")
        print("2 - Carregar Jogo")
        print("3 - Como Jogar")
        print("4 - Sair")
        misc.draw_line()

        choice = input("# ")

        if choice == "1":
            return self.new_game()
        elif choice == "2":
            return self.load_game()
        elif choice == "3":
            self.how_to_play()
        elif choice == "4":
            self.sair()
            misc.clear()

    def new_game(self):
        name = input("Digite seu nome: ")
        hero = Hero(name=name)
        seed_value = randint(0, 1000)

        return hero, seed_value

    def load_game(self):
        name_character = input("Insira o nome do personagem: ")
        hero, seed_value = misc.load_game(name_character)

        return hero, seed_value

    def how_to_play(self):
        pass

    def sair(self):
        choice_sair = input("# Realmente deseja sair (s/n)?: ")
        if choice_sair.lower() == "s":
            quit()
