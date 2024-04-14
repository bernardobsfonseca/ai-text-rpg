from random import randint
from Misc import misc
from States.menu_base import MenuBase


class MenuBattle(MenuBase):
    def __init__(self, hero, enemy):
        super().__init__()

        self.hero = hero
        self.enemy = enemy

        self.choice = ""

    def draw_menu(self):
        misc.draw_line()
        self.draw_status_hero()
        misc.draw_line()
        self.draw_status_enemy()
        misc.draw_line()

        print("1 - Atacar")
        print("2 - Usar poção")
        print("3 - Fugir")

        self.choice = input("# ")

        misc.draw_line()

        if self.choice == "1":
            self.hero.attack(self.enemy)
        elif self.choice == "2":
            self.hero.use_potion()
        elif self.choice == "3":
            chance = randint(0, 10)
            if chance >= 6:
                print(f"Você fugiu de {self.enemy.name}!")
                input("> ")
                return False
            else:
                print(f"Não conseguiu fugir!")
                input("> ")

        misc.draw_line()

        self.enemy_turn()

        return self.status_battle()

    def draw_status_hero(self):
        print(f"NOME: {self.hero.name}")
        print(f"HP: {self.hero.hp}")
        print(f"ATAQUE: {self.hero.atk}")
        print(f"POÇÕES: {self.hero.potions}")

    def draw_status_enemy(self):
        print(f"NOME: {self.enemy.name}")
        print(f"HP: {self.enemy.hp}")

    def enemy_turn(self):
        self.enemy.attack(self.hero)

    def status_battle(self):
        if self.hero.hp <= 0:
            print("morreu")
            self.enemy.reset_hp()
            return False
        elif self.enemy.hp <= 0:
            print("ganhou")
            self.enemy.reset_hp()
            return False

        return True
