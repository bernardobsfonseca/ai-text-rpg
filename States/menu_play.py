import time

from Ai.SceneAmbient.scene_ambient import SceneAmbient
from Ai.SceneAmbient.scene_ambient_modifiers import get_weather_modifier, get_day_time_modifier
from Characters import enemies
from Map.map import Map
from Misc import misc
from Misc.misc import save_game
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
        self.choice = ""

        self.scene_ambient = SceneAmbient()
        self.previous_terrain = ""

    def draw_menu(self):

        if not self.in_battle:
            if self.hero.alive is False:
                misc.clear()
                self.draw_death()
                input("> ")
                return False
            return self.draw_menu_play()
        else:
            self.in_battle = self.menu_battle.draw_menu()

    def draw_menu_play(self):
        misc.draw_line()
        self.draw_status_hero()
        misc.draw_line()
        self.draw_opcoes_hero()
        misc.draw_line()

        self.event_ambient()
        self.game_map.display_map()

        misc.draw_line()

        self.choice = input("# ")

        if self.choice == "0":
            save_game(self.hero, self.seed_value)
        elif self.choice == "1":
            if self.hero.y < self.map_y and self.hero.y > 0:
                self.hero.y -= 1
                self.step()
        elif self.choice == "2":
            if self.hero.x < self.map_x - 1:
                self.hero.x += 1
                self.step()
        elif self.choice == "3":
            if self.hero.y < self.map_y - 1:
                self.hero.y += 1
                self.step()
        elif self.choice == "4":
            if self.hero.x < self.map_x and self.hero.x > 0:
                self.hero.x -= 1
                self.step()
        elif self.choice == "5":
            self.hero.use_potion()

        return self.status_play()

    def step(self):
        self.game_map.construct_map(self.hero.x, self.hero.y)
        self.event()

    def event(self):
        seed_value = int(time.time())
        seed(seed_value)

        num = randint(0, 10)
        if num >= 9:
             self.battle_event()

    def event_ambient(self):
        weather = get_weather_modifier()
        terrain = self.game_map.current_tile
        day_time = get_day_time_modifier()
        print(f"{weather} {terrain} {day_time}")

        if self.previous_terrain != terrain:
            self.previous_terrain = terrain
            self.scene_ambient.create_scene(f"a {weather} {terrain} at {day_time}")
            print("\n")

    def battle_event(self):
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

    def status_play(self):
        if self.choice == "0":
            return False
        else:
            return True

    def draw_status_hero(self):
        print(f"LOC: {self.hero.x}, {self.hero.y}")
        print("STATUS")
        print(f"NOME: {self.hero.name}")
        print(f"HP: {self.hero.hp}")
        print(f"ATAQUE: {self.hero.atk}")
        print(f"POÇÕES: {self.hero.potions}")
        print(f"GEMS: {self.hero.gems}")

    def draw_opcoes_hero(self):
        print("1 - Norte")
        print("2 - Leste")
        print("3 - Sul")
        print("4 - Oeste")
        print("5 - Usar poção")
        print("0 - Salvar e sair")

    def draw_death(self):
        print("""
         __     ______  _    _   _____ _____ ______ _____  
         \ \   / / __ \| |  | | |  __ \_   _|  ____|  __ \ 
          \ \_/ / |  | | |  | | | |  | || | | |__  | |  | |
           \   /| |  | | |  | | | |  | || | |  __| | |  | |
            | | | |__| | |__| | | |__| || |_| |____| |__| |
            |_|  \____/ \____/  |_____/_____|______|_____/ 
        """)
