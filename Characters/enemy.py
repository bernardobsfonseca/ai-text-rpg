from Characters.character import Character


class Enemy(Character):
    def __init__(self, name, hp, atk)\
            -> None:
        super().__init__(name=name, hp=hp, atk=atk)

    def reset_hp(self):
        self.hp = self.max_hp
