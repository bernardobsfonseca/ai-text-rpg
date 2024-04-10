from Characters.character import Character


class Hero(Character):
    def __init__(self, name, hp, atk, potions=3, gems=30, x=0, y=0)\
            -> None:
        super().__init__(name=name, hp=hp, atk=atk)
        self.potions = potions
        self.gems = gems
        self.x = x
        self. y = y
