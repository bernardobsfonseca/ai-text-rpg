from random import randint
from Characters.hero import Hero
from Misc import misc
from States.menu_base import MenuBase


class MenuInicial(MenuBase):
    def __init__(self):
        super().__init__()

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
            return self.novo_jogo()
        elif choice == "2":
            return self.carregar_jogo()
        elif choice == "3":
            self.como_jogar()
        elif choice == "4":
            self.sair()
            misc.clear()

    def novo_jogo(self):
        name = input("Digite seu nome: ")
        hero = Hero(name=name, hp=30, atk=5)
        seed_value = randint(0, 1000)

        return hero, seed_value

    def carregar_jogo(self):
        name_character = input("Insira o nome do personagem: ")
        hero, seed_value = misc.load_game(name_character)

        return hero, seed_value

    def como_jogar(self):
        pass

    def sair(self):
        choice_sair = input("# Realmente deseja sair (s/n)?: ")
        if choice_sair.lower() == "s":
            quit()
