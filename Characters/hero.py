from Characters.character import Character


class Hero(Character):
    def __init__(self, name="Ulisses", hp=30, atk=5, potions=3,
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

    def sharpen_sword(self):
        self.atk += 5
        print(f"{self.name} attack has increased")
