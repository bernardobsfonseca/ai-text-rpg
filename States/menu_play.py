from Map.map import Map
from Misc import misc
from Misc.misc import save_game, clear
from random import randint, seed
from States.menu_base import MenuBase


class MenuPlay(MenuBase):
    def __init__(self, hero, seed_value):
        super().__init__()

        self.hero = hero
        self.seed_value = seed_value

        seed(self.seed_value)
        self.map_x = randint(30, 50)
        self.map_y = randint(10, 15)

        self.game_map = Map(self.map_x, self.map_y, self.seed_value, hero)

    def draw_menu(self):
        # mapa
        misc.draw_line()
        print(f"LOC: {self.hero.x}, {self.hero.y}")
        print("STATUS")
        print(f"NOME: {self.hero.name}")
        print(f"HP: {self.hero.hp}")
        print(f"ATAQUE: {self.hero.atk}")
        print(f"POÇÕES: {self.hero.potions}")
        print(f"GEMS: {self.hero.gems}")
        misc.draw_line()
        print("1 - Norte")
        print("2 - Leste")
        print("3 - Sul")
        print("4 - Oeste")
        print("5 - Usar poção")
        print("0 - Salvar e sair")
        misc.draw_line()

        # draw map
        self.game_map.display_map()
        misc.draw_line()

        clear()
        choice = input("# ")

        if choice == "0":
            save_game(self.hero, self.seed_value)
            clear()
            return False
        elif choice == "1":
            if self.hero.y < self.map_y and self.hero.y > 0:
                self.hero.y -= 1
                self.passo()
        elif choice == "2":
            if self.hero.x < self.map_x-1:
                self.hero.x += 1
                self.passo()
        elif choice == "3":
            if self.hero.y < self.map_y-1:
                self.hero.y += 1
                self.passo()
        elif choice == "4":
            if self.hero.x < self.map_x and self.hero.x > 0:
                self.hero.x -= 1
                self.passo()
        elif choice == "5":
            pass

    def passo(self):
        self.game_map.construct_map(self.hero.x, self.hero.y)
        self.encontro_batalha()

    def encontro_batalha(self):
        num = randint(0, 20)
        if num > 12:
            print(f"aaaaaaaaaaaaaaaaaaaa{num}aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
