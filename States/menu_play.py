import time
from Ai.SceneAmbient import scene_ambient as se
from Ai.SceneAmbient import scene_ambient_modifiers as ambient_modifiers
from Characters import enemies
from Characters.enemies import dragon
from Map.map import Map
from Misc import misc
from Misc.misc import save_game
from random import randint, seed
from States.menu_base import MenuBase
from States.menu_battle import MenuBattle
from States.menu_merchant import MenuMerchant


class MenuPlay(MenuBase):
    def __init__(self, hero, seed_value):
        super().__init__()

        self.menu_battle = None
        self.menu_merchant = None
        self.hero = hero
        self.seed_value = seed_value

        seed(self.seed_value)
        self.map_x = randint(30, 50)
        self.map_y = randint(10, 15)
        self.game_map = Map(self.map_x, self.map_y, self.seed_value, hero)

        self.in_battle_dragon = False
        self.in_battle = False
        self.in_merchant = False
        self.choice = ""

        self.previous_terrain = ""

    def draw_menu(self):
        if self.in_merchant:
            self.in_merchant = self.menu_merchant.draw_menu()
        elif self.in_battle:
            self.in_battle = self.menu_battle.draw_menu()
        elif self.in_battle_dragon:
            self.in_battle_dragon = self.menu_battle.draw_menu()
            if self.in_battle_dragon == 'win':
                misc.clear()
                self.draw_win()
                input(">")
                save_game(self.hero, self.seed_value)
                print('Game Saved!')
                input("> ")
                return False
            if self.in_battle_dragon is False:
                misc.clear()
                self.draw_death()
                input(">")
                return False
        elif not self.in_battle and not self.in_merchant:
            if self.hero.alive is False:
                misc.clear()
                self.draw_death()
                input(">")
                return False
            return self.draw_menu_play()

    def draw_menu_play(self):
        misc.draw_line()
        self.draw_status_hero()
        misc.draw_line()
        self.draw_opcoes_hero()
        misc.draw_line()

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
            input(">")

        return self.status_play()

    def step(self):
        self.game_map.construct_map(self.hero.x, self.hero.y)
        self.event_ambient()
        self.event_merchant()
        self.event_battle()
        self.dragon_battle()

    def event_ambient(self):
        weather = ambient_modifiers.get_weather_modifier()
        terrain = self.game_map.current_tile
        day_time = ambient_modifiers.get_day_time_modifier()

        if self.previous_terrain != terrain:
            self.previous_terrain = terrain
            se.scene_ambient.create_scene(f"a {weather} {terrain} at {day_time}")
            print('\n')
            input('> ')

    def event_battle(self):
        seed_value = int(time.time())
        seed(seed_value)

        num = randint(0, 40)
        if num >= 36:
            self.start_battle()

    def start_battle(self):
        seed_value = int(time.time())
        seed(seed_value)

        enemy_selected = self.select_enemy()
        self.menu_battle = MenuBattle(self.hero, enemy_selected,
                                        self.game_map.current_tile)
        self.in_battle = True

    def dragon_battle(self):
        if self.game_map.current_tile == 'dragon':
            self.menu_battle = MenuBattle(self.hero, dragon,
                                          self.game_map.current_tile)
            self.in_battle_dragon = True


    def event_merchant(self):
        if self.game_map.current_tile == "merchant":
            self.in_merchant = True
            self.menu_merchant = MenuMerchant(self.hero)

    def select_enemy(self):
        seed_value = int(time.time())
        seed(seed_value)
        
        return enemies.list_enemies[
            randint(0, len(enemies.list_enemies) - 1)
        ]

    def status_play(self):
        if self.choice == "0":
            return False
        else:
            return True

    def draw_status_hero(self):
        print(f"LOC: {self.hero.x}, {self.hero.y}")
        print("STATUS")
        print(f"NAME: {self.hero.name}")
        print(f"HP: {self.hero.hp}")
        print(f"ATTACK: {self.hero.atk}")
        print(f"POTIONS: {self.hero.potions}")
        print(f"GEMS: {self.hero.gems}")

    def draw_opcoes_hero(self):
        print("1 - North")
        print("2 - East")
        print("3 - South")
        print("4 - West")
        print("5 - Use potion")
        print("0 - Save and quit")

    def draw_death(self):
        print("""
         __     ______  _    _   _____ _____ ______ _____  
         | |   / / __ || |  | | |  __ |_   _|  ____|  __ | 
          | |_/ / |  | | |  | | | |  | || | | |__  | |  | |
           |   /| |  | | |  | | | |  | || | |  __| | |  | |
            | | | |__| | |__| | | |__| || |_| |____| |__| |
            |_|  |____| |____|  |_____|_____|______|_____| 
        """)

    def draw_win(self):
        print("""
         __     ______  _    _  __          _______ _   _ 
         | |   / / __ || |  | | | |        / /_   _| | | |
          | |_/ / |  | | |  | |  | |  /|  / /  | | |  || |
           |   /| |  | | |  | |   | |/  |/ /   | | | . ` |
            | | | |__| | |__| |    |  /|  /   _| |_| ||  |
            |_|  |____| |____|      |/  |/   |_____|_| |_|
        """)
