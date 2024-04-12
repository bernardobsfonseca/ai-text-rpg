from Misc import misc
from States.menu_base import MenuBase


class MenuBattle(MenuBase):
    def __init__(self, hero, enemy):
        super().__init__()

        self.hero = hero
        self.enemy = enemy

    def draw_menu(self):
        misc.draw_line()
        self.draw_status_hero()
        misc.draw_line()
        self.draw_status_enemy()
        misc.draw_line()

        # draw texto da batalha

        input("# ")
        return False

    def draw_status_hero(self):
        print(f"NOME: {self.hero.name}")
        print(f"HP: {self.hero.hp}")
        print(f"ATAQUE: {self.hero.atk}")
        print(f"POÇÕES: {self.hero.potions}")

    def draw_status_enemy(self):
        print(f"NOME: {self.enemy.name}")
        print(f"HP: {self.enemy.hp}")
