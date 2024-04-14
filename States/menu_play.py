import time

from Characters import enemies
from Map.map import Map
from Misc import misc
from Misc.misc import save_game, clear
from random import randint, seed
from States.menu_base import MenuBase
from States.menu_battle import MenuBattle


class MenuPlay(MenuBase):
    def __init__(self, hero, seed_value):
        super().__init__()

        self.menu_battle = None
        self.hero = hero
        self.seed_value = seed_value

        seed(self.seed_value)
        self.map_x = randint(30, 50)
        self.map_y = randint(10, 15)
        self.game_map = Map(self.map_x, self.map_y, self.seed_value, hero)

        self.in_battle = False

    def draw_menu(self):

        if not self.in_battle:
            return self.draw_menu_play()
        else:
            self.in_battle = self.menu_battle.draw_menu()

    def draw_menu_play(self):
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

        self.game_map.display_map()
        misc.draw_line()

        choice = input("# ")

        if choice == "0":
            save_game(self.hero, self.seed_value)
            return False
        elif choice == "1":
            if self.hero.y < self.map_y and self.hero.y > 0:
                self.hero.y -= 1
                self.passo()
        elif choice == "2":
            if self.hero.x < self.map_x - 1:
                self.hero.x += 1
                self.passo()
        elif choice == "3":
            if self.hero.y < self.map_y - 1:
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
        self.battle_chance()

    def battle_chance(self):
        seed_value = int(time.time())
        seed(seed_value)

        num = randint(0, 20)
        if num > 12:
            enemy_selected = self.select_enemy()
            self.menu_battle = MenuBattle(self.hero, enemy_selected)
            self.in_battle = True

    def select_enemy(self):
        return enemies.list_enemies[
            randint(0, len(enemies.list_enemies)-1)
        ]
