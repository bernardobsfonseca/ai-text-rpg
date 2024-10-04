from Characters.character import Character
from Misc import global_vars


class Hero(Character):
    def __init__(self, name="Ulisses", hp=40, atk=5, potions=3,
                 gems=30, x=0, y=0)\
            -> None:
        super().__init__(name=name, hp=hp, atk=atk)
        self.potions = potions
        self.gems = gems
        self.x = x
        self.y = y
        self.alive = True

    def use_potion(self):
        if self.potions > 0:
            self.hp += 15
            self.potions -= 1
            if self.hp > self.max_hp:
                self.hp = self.max_hp

        print(f"{self.name} used a potion")

    def buy_potions(self, times):
        self.gems -= times*global_vars.potion_price
        self.potions += 1 * times

    def sharpen_sword(self, times):
        self.gems -= times*global_vars.sharpen_price
        self.atk += 5 * times
